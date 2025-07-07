# Petstore REST Automation (Python)

Фреймворк для автоматизационного тестирования Swagger Petstore REST API на Python с использованием `pytest`, `requests`, `SQLAlchemy` и `jsonschema`.

## Содержание

* [Описание проекта](#описание-проекта)
* [Требования](#требования)
* [Установка](#установка)
* [Конфигурация](#конфигурация)
* [Структура проекта](#структура-проекта)
* [Запуск тестов](#запуск-тестов)
* [Отчётность](#отчётность)
* [Расширение](#расширение)

## Описание проекта

Проект демонстрирует пример построения REST-фреймворка для автоматизации API-тестов и интеграционных проверок данных в базе:

* **HTTP-клиент** (`src/client.py`) с методами GET/POST/PUT/DELETE и валидацией JSON-ответов по схемам.
* **Доступ к БД** (`src/db.py`) через SQLAlchemy с функцией получения питомца по ID.
* **Схемы** (`src/schemas/*.json`) для проверки корректности структуры ответов.
* **Тесты** (`tests/`) с фикстурами и параметризацией через `pytest`.

## Требования

* Python 3.8+
* Docker (для запуска Petstore API и Postgres)
* Git

## Установка

1. Клонировать репозиторий:

   ```bash
   git clone https://github.com/RomanRyabinkin/petstore-rest-automation-python.git
   cd petstore-rest-automation-python
   ```
2. Создать и активировать виртуальное окружение:

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Linux/macOS
   .\.venv\Scripts\Activate.ps1 # Windows PowerShell
   ```
3. Установить зависимости:

   ```bash
   pip install -r requirements.txt
   ```

## Конфигурация

В файле `config.yaml` задаются:

```yaml
api:
  base_url: http://localhost:8080/api/v3
  timeout: 5

db:
  url: postgresql://test:test@localhost:5432/petstore
```

При необходимости можно переопределить `base_url` через переменную окружения `BASE_URL` или опцию `--base-url` pytest.

## Структура проекта

```text
petstore-rest-automation-python/
├── .venv/                      # виртуальное окружение
├── src/
│   ├── client.py              # HTTP-клиент + валидация
│   ├── db.py                  # доступ к БД
│   └── schemas/               # JSON Schema для ответов
├── tests/
│   ├── conftest.py            # фикстуры и ожидание API
│   └── test_pet_crud.py       # примеры CRUD-тестов
├── config.yaml                # конфигурация API и БД
├── requirements.txt           # зависимости
├── pytest.ini                 # настройки pytest
└── README.md                  # этот файл
```

## Запуск тестов

1. Запустить сервисы:

   ```bash
   docker run -d --name petstore -p 8080:8080 swaggerapi/petstore3:unstable
   docker run -d --name petstore-db -e POSTGRES_USER=test \
     -e POSTGRES_PASSWORD=test -e POSTGRES_DB=petstore \
     -p 5432:5432 postgres:15
   ```
2. Запустить тесты:

   ```bash
   pytest
   ```

## Отчётность

* Встроенный отчёт `pytest -ra -q`.
* Для покрытия можно установить `pytest-cov` и запускать:

  ```bash
  pytest --cov=src --cov-report=xml
  ```

## Расширение

* Добавить сервисные классы для `/user`, `/store/order`.
* Реализовать unit-тесты для методов `ApiClient` и `db`.
* Интегрировать CI (GitHub Actions).
* Параметризовать тесты по различным сценариям и статусам питомца.
