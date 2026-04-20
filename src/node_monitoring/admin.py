from django.contrib import admin
from node_monitoring import models


@admin.register(models.Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'expected_os_name', 'expected_cpu_name', 'max_cpu_load', 'min_free_disk_gb',)
    search_fields = ('name',)
    list_filter = ('expected_os_name', 'expected_cpu_name', 'max_cpu_load', 'min_free_disk_gb',)


@admin.register(models.MetricType)
class MetricTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_name', 'collect_interval_minutes',)
    search_fields = ('name',)
    list_filter = ('collect_interval_minutes',)
