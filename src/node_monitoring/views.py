from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

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
    - node: точное имя узла
    - metric_type: точное имя типа метрики
    - is_valid: true/false
    - created_at_gte: дата и время
    - created_at_lte: дата и время
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
