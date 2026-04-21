from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.response import Response

from node_monitoring import models, pagination, serializers
from node_monitoring.filters import CustomOrderingFilter, NodeMetricHistoryFilter


class NodeListView(ListCreateAPIView):
    """
    Представление для просмотра списка отслеживаемых устройств и добавления новых

    Поддерживаемые методы:
    - GET: Возвращает список всех устройств
    - POST: Создает новое устройсво в списке доступных устройств для мониторинга в сети
    """

    serializer_class = serializers.NodeListSerializer
    queryset = models.Node.objects.all()


class NodeDetailView(RetrieveUpdateDestroyAPIView):
    """
    Представление для получения, изменения и удаления устройства

    Поддерживаемые методы:
    - GET: Возвращает детальную информацию об устройстве
    - PUT / PATCH: Обновляет данные устройства
    - DELETE: Удаляет устройство из системы мониторинга
    """

    serializer_class = serializers.NodeDetailSerializer
    queryset = models.Node.objects.all()
    lookup_field = "name"


class MetricTypeListView(ListCreateAPIView):
    """
    Представление для просмотра списка доступных метрик и добавления новых

    Поддерживаемые методы:
    - GET: Возвращает список всех доступных метрик
    - POST: Создает новую метрики для отслеживания на устройствах
    """

    serializer_class = serializers.MetricTypeListSerializer
    queryset = models.MetricType.objects.all()


class MetricTypeDetailView(RetrieveUpdateDestroyAPIView):
    """
    Представление для получения, изменения и удаления метрики

    Поддерживаемые методы:
    - GET: Возвращает детальную информацию о метрике
    - PUT / PATCH: Обновляет данные метрики
    - DELETE: Удаляет метрику из списка доступных
    """

    serializer_class = serializers.MetricTypeDetailSerializer
    queryset = models.MetricType.objects.all()
    lookup_field = "name"


class NodeMetricHistoryListView(ListAPIView):
    """
    Представление для получения списка записей истории мониторинга

    Поддерживаемые методы:
    - GET: Возвращает список записей (NodeMetricHistory)

    Поддерживаемые фильтры (через query parameters):
    - node: точное название устройства
    - metric_type: точное название метрики
    - is_valid: true/false
    - created_at_gte: дата и время (не ранее)
    - created_at_lte: дата и время (не позднее)
    """

    serializer_class = serializers.NodeMetricHistoryListSerializer
    queryset = models.NodeMetricHistory.objects.all()
    pagination_class = pagination.ResultsPagination
    filter_backends = [
        DjangoFilterBackend,
        CustomOrderingFilter,
    ]
    filterset_class = NodeMetricHistoryFilter
    ordering_fields = ["created_at"]
    ordering = ["-created_at"]


class NodeMetricHistoryCreateView(CreateAPIView):
    """
    Представление для создания новой записи истории мониторинга.

    Поддерживаемые методы:
    - POST: Создаёт новую запись истории
    """

    serializer_class = serializers.NodeMetricHistoryCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        node = models.Node.objects.get(name=serializer.validated_data["node_name"])
        metric_type = models.MetricType.objects.get(name=serializer.validated_data["metric_type_name"])
        value = serializer.validated_data["value"]

        history = models.NodeMetricHistory.objects.create(
            node=node,
            metric_type=metric_type,
            value=value,
            is_valid=True,
            validation_message="",
        )
        output_serializer = serializers.NodeMetricHistoryListSerializer(instance=history)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)
