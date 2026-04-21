# NetworkDevicesMetrics



## Установка и запуск
Клонировать репозиторий.

### Установка через poetry
1. Установить зависимости: `poetry install`
2. Применить миграции: `poetry run python src/manage.py migrate`
3. Загрузить типы метрик: `poetry run python src/manage.py load_metric_types`
4. Запустить сервер: `poetry run python src/manage.py runserver`

### Установка через pip
1. Создать виртуальное окружение
2. Установить зависимости: `pip install -r requirements.txt`
3. Применить миграции: `python src/manage.py migrate`
4. Загрузить типы метрик: `python src/manage.py load_metric_types`
5. Запустить сервер: `python src/manage.py runserver`

## Создание администратора Django
Создать администратора: `python manage.py createsuperuser`

## API Endpoints

| Метод | URL | Описание |
|-------|-----|----------|
| GET | /su/ | Панель администратора Django |
| GET | /api/schema/ | API документация в формате JSON/YAML |
| GET | /api/swagger/ | API документация в формате Swagger-UI |
| GET | /api/redoc/ | API документация в формате ReDoc |
| GET | /api/nodes/ | Список всех устройств |
| POST | /api/nodes/ | Создать новое устройство |
| GET | /api/nodes/{name}/ | Детали устройства |
| PUT/PATCH | /api/nodes/{name}/ | Обновить данные устройства |
| GET | /api/metric-types/ | Список метрик |
| POST | /api/metric-types/ | Создать новую метрику |
| GET | /api/metric-types/{name}/ | Детали метрики |
| PUT/PATCH | /api/metric-types/{name}/ | Обновить данные метрики |
| DELETE | /api/metric-types/{name}/ | Удалить метрику |
| GET | /api/history/ | Список всех записей мониторинга устройств |
| POST | /api/history/create/ | Создать новую запись в списке записей мониторинга устройств |
