from rest_framework import serializers

from node_monitoring import models


class NodeDetailSerializer(serializers.ModelSerializer):
    """
    Сериализатор для детальной информации об устройстве
    """

    class Meta:
        model = models.Node
        fields = [
            "id",
            "name",
            "expected_os_name",
            "expected_cpu_name",
            "max_cpu_load",
            "min_free_disk_gb",
        ]
        read_only_fields = [
            "id",
        ]


class NodeListSerializer(serializers.ModelSerializer):
    """
    Сериализатор для списка устройств
    """

    url = serializers.HyperlinkedIdentityField(
        view_name="node-detail", read_only=True, lookup_field="name", lookup_url_kwarg="name"
    )

    class Meta:
        model = models.Node
        fields = [
            "url",
            "id",
            "name",
            "expected_os_name",
            "expected_cpu_name",
            "max_cpu_load",
            "min_free_disk_gb",
        ]
        read_only_fields = [
            "id",
        ]


class MetricTypeDetailSerializer(serializers.ModelSerializer):
    """
    Сериализатор для детальной информации о метрике
    """

    class Meta:
        model = models.MetricType
        fields = [
            "id",
            "name",
            "display_name",
            "collect_interval_minutes",
        ]
        read_only_fields = [
            "id",
        ]


class MetricTypeListSerializer(serializers.ModelSerializer):
    """
    Сериализатор для списка метрик
    """

    url = serializers.HyperlinkedIdentityField(
        view_name="metric_types-detail", read_only=True, lookup_field="name", lookup_url_kwarg="name"
    )

    class Meta:
        model = models.MetricType
        fields = [
            "url",
            "id",
            "name",
            "display_name",
            "collect_interval_minutes",
        ]
        read_only_fields = [
            "id",
        ]


class NodeMetricHistoryListSerializer(serializers.ModelSerializer):
    """Серелизатор для списка записей (NodeMetricHistory)"""

    node = NodeDetailSerializer(read_only=True)
    metric_type = MetricTypeDetailSerializer(read_only=True)

    class Meta:
        model = models.NodeMetricHistory
        fields = [
            "id",
            "node",
            "metric_type",
            "value",
            "created_at",
            "is_valid",
            "validation_message",
        ]
        read_only_fields = [
            "id",
            "value",
            "created_at",
            "is_valid",
            "validation_message",
        ]


class NodeMetricHistoryCreateSerializer(serializers.Serializer):
    """Серелизатор для создания новой записи в списке NodeMetricHistory"""

    node_name = serializers.CharField(max_length=100)
    metric_type_name = serializers.CharField(max_length=100)
    value = serializers.CharField(max_length=255)

    def validate_node_name(self, value):
        if not models.Node.objects.filter(name=value).exists():
            raise serializers.ValidationError(f"Устройство '{value}' не найдено")
        return value

    def validate_metric_type_name(self, value):
        if not models.MetricType.objects.filter(name=value).exists():
            raise serializers.ValidationError(f"Метрика '{value}' не найдена")
        return value
