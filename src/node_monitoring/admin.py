from django.contrib import admin
from .models import Node

@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'expected_os_name', 'expected_cpu_name', 'max_cpu_load', 'min_free_disk_gb',)
    search_fields = ('name',)
    list_filter = ('expected_os_name', 'expected_cpu_name', 'max_cpu_load', 'min_free_disk_gb',)