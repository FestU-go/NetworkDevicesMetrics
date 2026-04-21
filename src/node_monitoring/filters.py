from django_filters import rest_framework as drf_filters
from rest_framework import filters

from node_monitoring.models import NodeMetricHistory


class NodeMetricHistoryFilter(drf_filters.FilterSet):
    """Класс фильтрации списка записей NodeMetricHistory"""

    node = drf_filters.CharFilter(
        field_name="node__name",
        lookup_expr="exact",
        label="Устройство",
    )
    metric_type = drf_filters.CharFilter(
        field_name="metric_type__name",
        lookup_expr="exact",
        label="Метрика",
    )
    is_valid = drf_filters.ChoiceFilter(
        choices=[(True, "Успешно"), (False, "Не успешно")],
        empty_label="Все",
        method="filter_is_valid",
    )
    created_at_gte = drf_filters.DateTimeFilter(
        field_name="created_at",
        lookup_expr="gte",
        label="Дата и время (не ранее)",
    )
    created_at_lte = drf_filters.DateTimeFilter(
        field_name="created_at",
        lookup_expr="lte",
        label="Дата и время (не позднее)",
    )

    def filter_is_valid(self, queryset, name, value):
        if value is None:
            return queryset
        return queryset.filter(is_valid=value)

    class Meta:
        model = NodeMetricHistory
        fields = [
            "node",
            "metric_type",
            "is_valid",
            "created_at_gte",
            "created_at_lte",
        ]


class CustomOrderingFilter(filters.OrderingFilter):
    """Класс кастомной сортировки на русском языке (по убыыванию/по возрастанию)"""

    ordering_title = "Сортировка"

    def get_template_context(self, request, queryset, view):
        current = self.get_ordering(request, queryset, view)
        current = None if not current else current[0]
        options = []
        context = {
            "request": request,
            "current": current,
            "param": self.ordering_param,
        }
        for key, label in self.get_valid_fields(queryset, view, context):
            options.append((key, f"{label} — по возрастанию"))
            options.append((f"-{key}", f"{label} — по убыванию"))
        context["options"] = options
        return context
