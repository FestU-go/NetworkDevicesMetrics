from django.db import models


class Node(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название устройства")
    expected_os_name = models.CharField(max_length=100, blank=True, default='', verbose_name="Название ОС")
    expected_cpu_name = models.CharField(max_length=100, blank=True, default='', verbose_name="Название процессора")
    max_cpu_load = models.FloatField(default=80.0, verbose_name="Максимальная допустимая нагрузка CPU (%)")
    min_free_disk_gb = models.IntegerField(default=10, verbose_name="Минимальное свободное место (ГБ)")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Node"
