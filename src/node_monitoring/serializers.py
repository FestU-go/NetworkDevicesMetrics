from rest_framework import serializers
from node_monitoring.models import Node, MetricType

class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = ['id', 'name', 'expected_os_name', 'expected_cpu_name', 'max_cpu_load', 'min_free_disk_gb']
        read_only_fields = ['id']

class NodeListSerializer(NodeSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="node-detail", read_only=True, lookup_field="name", lookup_url_kwarg="name")

    class Meta:
        model = Node
        fields = ['url', 'id', 'name', 'expected_os_name', 'expected_cpu_name', 'max_cpu_load', 'min_free_disk_gb']
        read_only_fields = ['id']

class MetricTypeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetricType
        fields = ['id', 'name', 'display_name', 'collect_interval_minutes',]
        read_only_fields = ['id']