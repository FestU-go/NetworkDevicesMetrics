from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView,
)

from node_monitoring import models
from node_monitoring import serializers

class NodeListView(ListCreateAPIView):
    serializer_class = serializers.NodeListSerializer
    queryset = models.Node.objects.all()

class NodeDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.NodeDetailSerializer
    queryset = models.Node.objects.all()
    lookup_field = "name"

class MetricTypeListView(ListCreateAPIView):
    serializer_class = serializers.MetricTypeListSerializer
    queryset = models.MetricType.objects.all()

class MetricTypeDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.MetricTypeDetailSerializer
    queryset = models.MetricType.objects.all()
    lookup_field = "name"
