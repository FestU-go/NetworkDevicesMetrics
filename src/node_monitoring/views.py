from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateAPIView,
)

from node_monitoring import models
from node_monitoring import serializers

class NodeListView(ListCreateAPIView):
    serializer_class = serializers.NodeListSerializer
    queryset = models.Node.objects.all()

class NodeDetailView(RetrieveUpdateAPIView):
    serializer_class = serializers.NodeSerializer
    queryset = models.Node.objects.all()
    lookup_field = "name"

class MetricTypeListView(ListCreateAPIView):
    serializer_class = serializers.MetricTypeListSerializer
    queryset = models.MetricType.objects.all()