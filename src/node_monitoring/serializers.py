from rest_framework import serializers

from node_monitoring.models import MetricType, Node


class NodeDetailSerializer(serializers.ModelSerializer):
    """
    Сериализатор для детальной информации об устройстве
    """

    class Meta:
        model = Node
        fields = ["id", "name", "expected_os_name", "expected_cpu_name", "max_cpu_load", "min_free_disk_gb"]
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
        model = Node
        fields = ["url", "id", "name", "expected_os_name", "expected_cpu_name", "max_cpu_load", "min_free_disk_gb"]
        read_only_fields = [
            "id",
        ]


class MetricTypeDetailSerializer(serializers.ModelSerializer):
    """
    Сериализатор для детальной информации о метрике
    """

    class Meta:
        model = MetricType
        fields = [
            "id",
            "name",
            "display_name",
            "collect_interval_minutes",
        ]
        read_only_fields = ["id"]


class MetricTypeListSerializer(serializers.ModelSerializer):
    """
    Сериализатор для списка метрик
    """

    url = serializers.HyperlinkedIdentityField(
        view_name="metric_types-detail", read_only=True, lookup_field="name", lookup_url_kwarg="name"
    )

    class Meta:
        model = MetricType
        fields = [
            "url",
            "id",
            "name",
            "display_name",
            "collect_interval_minutes",
        ]
        read_only_fields = ["id"]
