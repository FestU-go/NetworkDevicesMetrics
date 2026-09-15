from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


def root_view(request):
    return JsonResponse(
        {
            "service": "node_monitoring",
            "docs": "/api/swagger/",
            "redoc": "/api/redoc/",
        }
    )


urlpatterns = [
    path("", root_view, name="root"),
    path("su/", admin.site.urls),
    path("api/", include("node_monitoring.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger"),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]
