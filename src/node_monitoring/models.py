from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Node(models.Model):
    """Модель сетевого устройства для мониторинга"""

    LINUX_OS = "Linux"
    WINDOWS_OS = "Windows"

    OS_CHOICES = [
        (LINUX_OS, "Linux"),
        (WINDOWS_OS, "Windows"),
    ]

    INTEL_CPU = "Intel"
    AMD_CPU = "AMD"

    CPU_CHOICES = [
        (INTEL_CPU, "Intel"),
        (AMD_CPU, "AMD"),
    ]

    name = models.CharField(max_length=100, unique=True, verbose_name="Название устройства")
    expected_os_name = models.CharField(
        max_length=100, choices=OS_CHOICES, blank=True, default="", verbose_name="Название ОС"
    )
    expected_cpu_name = models.CharField(
        max_length=100, choices=CPU_CHOICES, blank=True, default="", verbose_name="Название процессора"
    )
    max_cpu_load = models.FloatField(
        default=80.0,
        validators=[MinValueValidator(0.0), MaxValueValidator(100.0)],
        verbose_name="Максимальная допустимая нагрузка CPU (%)",
    )
    min_free_disk_gb = models.IntegerField(default=10, verbose_name="Минимальное свободное место (ГБ)")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Node"


class MetricType(models.Model):
    """Модель метрики, по которой можно отслеживать устройства"""

    name = models.CharField(max_length=100, unique=True, verbose_name="Название метрики")
    display_name = models.CharField(max_length=100, verbose_name="Отображаемое название метрики")
    collect_interval_minutes = models.IntegerField(
        validators=[MinValueValidator(1, message="Интервал должен быть больше 0")],
        verbose_name="Интервал сбора (минуты)",
    )

    def __str__(self):
        return f"name: {self.name}, display_name: {self.display_name}"

    class Meta:
        verbose_name = "MetricType"


class NodeMetricHistory(models.Model):
    """Модель для журналирования истории мониторинга Node по MetricType"""

    node = models.ForeignKey(Node, on_delete=models.CASCADE, related_name="metric_history", verbose_name="Устройство")
    metric_type = models.ForeignKey(MetricType, on_delete=models.CASCADE, verbose_name="Метрика")
    value = models.CharField(max_length=255, verbose_name="Текущее значение метрики")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    is_valid = models.BooleanField(default=False, verbose_name="Успешность")
    validation_message = models.CharField(max_length=255, blank=True, verbose_name="Дополнительная информация")

    class Meta:
        verbose_name = "История метрики"
        verbose_name_plural = "Истории метрик"
        indexes = [
            models.Index(fields=["node", "metric_type", "-created_at"]),
            models.Index(fields=["-created_at"]),
        ]
