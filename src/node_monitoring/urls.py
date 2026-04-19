from django.urls import path

from node_monitoring import views

urlpatterns = [
    path("nodes/", views.NodeListView.as_view(), name="node-list-create"),
    path("nodes/<str:name>/", views.NodeDetailView.as_view(), name="node-detail"),
]
