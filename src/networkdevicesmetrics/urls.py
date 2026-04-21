from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("su/", admin.site.urls),
    path("api/", include("node_monitoring.urls")),
]
