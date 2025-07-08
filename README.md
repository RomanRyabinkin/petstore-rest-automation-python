# Petstore REST Automation (Python)

Фреймворк для автоматизационного тестирования Swagger Petstore REST API на Python с использованием:

* `pytest` + `allure-pytest`
* `requests`
* `SQLAlchemy`
* `jsonschema`

## Содержание

* [Описание проекта](#описание-проекта)
* [Требования](#требования)
* [Установка](#установка)
* [Конфигурация](#конфигурация)
* [Структура проекта](#структура-проекта)
* [Запуск тестов](#запуск-тестов)
* [CI / GitHub Actions](#ci--github-actions)
* [Отчётность](#отчётность)
* [Расширение и поддержка](#расширение-и-поддержка)

## Описание проекта

Проект демонстрирует построение расширяемого REST-фреймворка с:

* **HTTP-клиентом** (`src/client.py`): методы `get`, `post`, `put`, `delete`,
  валидация JSON-ответов по JSON Schema (`src/schemas/*.json`).
* **Доступом к БД** (`src/db.py`): SQLAlchemy, фикстуры для подготовки схемы и синхронизации данных.
* **Динамическими тестовыми данными** (`tests/data.py`): фабрики `make_user()`, `make_order()`.
* **Константами** (`tests/constants.py`): ключевые строки и префиксы ответов.
* **Тестами** (`tests/`): позитивные и негативные сценарии для `/pet`, `/user`, `/store/order`.
* **Allure** для удобного HTML-отчёта.

## Требования

* Python 3.8+
* Docker (Petstore API и Postgres)
* Git

## Установка

```bash
git clone https://github.com/RomanRyabinkin/petstore-rest-automation-python.git
cd petstore-rest-automation-python
python -m venv .venv
source .venv/bin/activate      # Linux/macOS
.\.venv\Scripts\Activate.ps1 # Windows PowerShell
pip install -r requirements.txt
```

> В `requirements.txt` добавлены: `pytest`, `pytest-cov`, `allure-pytest`, `requests`, `PyYAML`, `jsonschema`, `SQLAlchemy`, `psycopg2-binary`.

## Конфигурация

Файл `config.yaml` задаёт:

```yaml
api:
  base_url: http://localhost:8080/api/v3
  timeout: 5

db:
  url: postgresql://test:test@localhost:5432/petstore
```

* Можно переопределить `api.base_url` через опцию `--base-url` pytest.

## Структура проекта

```
petstore-rest-automation-python/
├── .github/                   # CI/CD workflows
│   └── workflows/ci.yml
├── .venv/                     # виртуальное окружение
├── src/
│   ├── client.py             # HTTP-клиент + JSON Schema
│   ├── db.py                 # SQLAlchemy + фикстуры и схема
│   └── schemas/              # JSON Schema files
├── tests/
│   ├── data.py               # фабрики make_user, make_order
│   ├── constants.py          # LOGIN_SUCCESS_PREFIX и др.
│   ├── conftest.py           # фикстуры: wait_for_api, new_pet, init_db_schema
│   ├── test_pet_crud.py      # CRUD и негативные /pet
│   ├── test_pet_negative.py  # расширенные негативные /pet
│   ├── test_user_crud.py     # CRUD & дополнительные /user
│   ├── test_user_negative.py # негативные /user
├── config.yaml               # настройки API и БД
├── requirements.txt          # зависимости
├── pytest.ini                # настройки pytest & markers
└── README.md                 # документация проекта
```

## Запуск тестов

1. Поднимите сервисы:

   ```bash
   docker run -d --name petstore -p 8080:8080 swaggerapi/petstore3:unstable
   docker run -d --name petstore-db \
     -e POSTGRES_USER=test -e POSTGRES_PASSWORD=test \
     -e POSTGRES_DB=petstore -p 5432:5432 postgres:15
   ```
2. Запустите тесты и сохраните результаты Allure:

   ```bash
   pytest --maxfail=1 -q \
          --cov=src --cov-report=xml \
          --alluredir=allure-results
   ```

## CI / GitHub Actions

В `.github/workflows/ci.yml`:

* Запуск на любые ветки (`push: branches: ['**']`).
* Сервисы: Postgres и Swagger Petstore.
* Установка зависимостей + `allure-pytest`.
* Запуск `pytest` с `--alluredir`.
* Загрузка артефактов: Codecov и Allure (через `actions/upload-artifact@v4`).

## Отчётность

* **Coverage**: `coverage.xml` → Codecov.
* **Allure**: результат в `allure-results/`, частый HTML-отчёт:

  ```bash
  allure serve allure-results
  ```

## Расширение и поддержка

* Добавить unit-тесты и мокирование (для `client` и `db`).
* Поддержать окружения (staging, prod) через env-variables.
* Развертывание докера (docker-compose) для локальной инсталляции всех сервисов.

---

*Автор: Роман Рябинкин*
