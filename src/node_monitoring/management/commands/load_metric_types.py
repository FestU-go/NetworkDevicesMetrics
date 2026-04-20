import json
from pathlib import Path

from django.core.management.base import BaseCommand

from node_monitoring.models import MetricType

DEFAULT_DATA = [
    {"name": "cpu_name", "display_name": "Название процессора", "collect_interval_minutes": 1440},
    {"name": "cpu_load", "display_name": "Нагрузка CPU", "collect_interval_minutes": 5},
    {"name": "os_name", "display_name": "Название ОС", "collect_interval_minutes": 720},
    {"name": "free_disk", "display_name": "Свободный диск (ГБ)", "collect_interval_minutes": 60},
]


class Command(BaseCommand):
    """Команда для загрузки типов метрик в базу данных"""

    help = "Загружает типы метрик из fixtures/metric_types.json или использует значения по умолчанию (DEFAULT_DATA)"

    def _get_data(self) -> list[dict]:
        """Возвращает список словарей с данными метрик"""

        file_path = Path(__file__).resolve().parent.parent.parent / "fixtures" / "metric_types.json"
        try:
            with open(file_path, encoding="utf-8") as f:
                data = json.load(f)
            self.stdout.write(self.style.SUCCESS(f"Загружено из {file_path}"))
            return data
        except (OSError, json.JSONDecodeError) as e:
            self.stdout.write(
                self.style.WARNING(f"Не удалось загрузить {file_path}: {e}. Будут загружены значения по умолчанию.")
            )
            return DEFAULT_DATA

    def handle(self, *args, **options) -> None:
        """Функция загрузки метрик в БД"""
        data = self._get_data()
        for item in data:
            try:
                obj, created = MetricType.objects.get_or_create(
                    name=item["name"],
                    defaults={
                        "display_name": item["display_name"],
                        "collect_interval_minutes": item["collect_interval_minutes"],
                    },
                )
                status = "Создана" if created else "Уже существует"
                self.stdout.write(self.style.SUCCESS(f"{status}: {obj.name}"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Ошибка при обработке {item.get('name', '?')}: {e}"))
