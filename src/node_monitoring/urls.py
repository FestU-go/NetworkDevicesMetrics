from django.urls import path

from node_monitoring import views

urlpatterns = [
    path("nodes/", views.NodeListView.as_view(), name="node-list-create"),
    path("nodes/<str:name>/", views.NodeDetailView.as_view(), name="node-detail"),
    path("metric_types/", views.MetricTypeListView.as_view(), name="metric-types-list-create"),
    path("metric_types/<str:name>/", views.MetricTypeDetailView.as_view(), name="metric_types-detail"),
    path("history/", views.NodeMetricHistoryListView.as_view(), name="history-list"),
]
