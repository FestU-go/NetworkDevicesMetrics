# NetworkDevicesMetrics



## Установка и запуск
Клонировать репозиторий.

### Установка через poetry:
1. Установить зависимости: `poetry install`
2. Применить миграции: `poetry run python src/manage.py migrate`
3. Загрузить типы метрик: `poetry run python src/manage.py load_metric_types`
4. Запустить сервер: `poetry run python src/manage.py runserver`

### Установка через pip:
1. Создать виртуальное окружение
2. Установить зависимости: `pip install -r requirements.txt`
3. Применить миграции: `python src/manage.py migrate`
4. Загрузить типы метрик: `python src/manage.py load_metric_types`
5. Запустить сервер: `python src/manage.py runserver`



## API Endpoints

| Метод | URL | Описание |
|-------|-----|----------|
| GET | /api/nodes/ | Список всех узлов |
| POST | /api/nodes/ | Создать новый узел |
| GET | /api/nodes/{name}/ | Детали узла |
| PUT/PATCH | /api/nodes/{name}/ | Обновить узел |
| GET | /api/metric-types/ | Список типов метрик |
| POST | /api/metric-types/ | Создать новый тип метрики |
| GET | /api/metric-types/{name}/ | Детали типа метрики |
| PUT/PATCH | /api/metric-types/{name}/ | Обновить тип метрики |
| DELETE | /api/metric-types/{name}/ | Удалить тип метрики |
