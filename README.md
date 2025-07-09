# Petstore REST Automation (Python)

## 🇬🇧 English

A Python-based, extensible framework for automating tests against the Swagger Petstore REST API using:

- **pytest** + **allure-pytest**  
- **requests**  
- **SQLAlchemy**  
- **jsonschema**

### Table of Contents

- [Project Description](#project-description)  
- [Requirements](#requirements)  
- [Installation](#installation)  
- [Configuration](#configuration)  
- [Project Structure](#project-structure)  
- [Running Tests](#running-tests)  
- [CI / GitHub Actions](#ci--github-actions)  
- [Reporting](#reporting)  
- [Extension & Maintenance](#extension--maintenance)  

### Project Description

This project demonstrates building an extensible REST-API test framework with:

- **HTTP Client** (`src/client.py`):  
  Methods `get`, `post`, `put`, `delete` and JSON Schema validation (`src/schemas/*.json`).  
- **Database Access** (`src/db.py`):  
  SQLAlchemy integration, fixtures for schema setup and data sync.  
- **Dynamic Test Data** (`tests/data.py`):  
  Factory functions `make_user()`, `make_order()`.  
- **Constants** (`tests/constants.py`):  
  Key response prefixes and strings.  
- **Tests** (`tests/`):  
  Positive and negative scenarios for `/pet`, `/user`, `/store/order`.  
- **Allure** for rich HTML reporting.

### Requirements

- Python 3.8+  
- Docker (Petstore API & Postgres)  
- Git  

### Installation

```bash
git clone https://github.com/RomanRyabinkin/petstore-rest-automation-python.git
cd petstore-rest-automation-python
python -m venv .venv
source .venv/bin/activate      # Linux/macOS
.\.venv\Scripts\Activate.ps1   # Windows PowerShell
pip install -r requirements.txt
```

> **requirements.txt** includes:  
> `pytest`, `pytest-cov`, `allure-pytest`, `requests`, `PyYAML`, `jsonschema`, `SQLAlchemy`, `psycopg2-binary`

### Configuration

Edit **config.yaml**:

```yaml
api:
  base_url: http://localhost:8080/api/v3
  timeout: 5

db:
  url: postgresql://test:test@localhost:5432/petstore
```

You can override `api.base_url` with `--base-url` pytest option.

### Project Structure

```
petstore-rest-automation-python/
├── .github/                   # CI/CD workflows
│   └── workflows/ci.yml
├── .venv/                     # virtualenv
├── src/
│   ├── client.py              # HTTP client + JSON Schema
│   ├── db.py                  # SQLAlchemy + DB access
│   └── schemas/               # JSON Schema files
├── tests/
│   ├── data.py                # make_user, make_order factories
│   ├── constants.py           # key prefixes (e.g. LOGIN_SUCCESS_PREFIX)
│   ├── conftest.py            # fixtures: wait_for_api, new_pet, init_db_schema
│   ├── test_pet_crud.py       # CRUD & negative tests for /pet
│   ├── test_pet_negative.py   # extended negative /pet scenarios
│   ├── test_user_crud.py      # CRUD & extra tests for /user
│   ├── test_user_negative.py  # negative /user scenarios
│   ├── test_store_order.py    # CRUD & negative for /store/order
│   └── test_store_negative.py # negative /store/order scenarios
├── config.yaml                # API & DB settings
├── requirements.txt           # dependencies
├── pytest.ini                 # pytest settings & markers
└── README.md                  # this file
```

### Running Tests

1. Start services:

   ```bash
   docker run -d --name petstore -p 8080:8080 swaggerapi/petstore3:unstable
   docker run -d --name petstore-db      -e POSTGRES_USER=test -e POSTGRES_PASSWORD=test      -e POSTGRES_DB=petstore -p 5432:5432 postgres:15
   ```

2. Run tests & collect Allure results:

   ```bash
   pytest --maxfail=1 -q           --cov=src --cov-report=xml           --alluredir=allure-results
   ```

### CI / GitHub Actions

Workflow at `.github/workflows/ci.yml`:

- Triggers on **all branches** (`push: branches: ['**']`) and PRs to **main**.  
- Spins up Postgres and Petstore containers.  
- Installs dependencies including `allure-pytest`.  
- Runs `pytest` with coverage & Allure result directory.  
- Uploads Codecov report and Allure artifacts via `actions/upload-artifact@v4`.

### Reporting

- **Coverage**: `coverage.xml` → Codecov  
- **Allure**: HTML report from `allure-results/`:

  ```bash
  allure serve allure-results
  ```

### Extension & Maintenance

- Add unit tests & mocks for `client` and `db`.  
- Support multiple environments (staging, prod) via environment variables.  
- Integrate Slack/Teams notifications on pipeline status.  
- Provide a `docker-compose.yml` for full local setup of API + DB.

---

**Author: Роман Рябинкин**

---

## 🇷🇺 Русский

Фреймворк для автоматизационного тестирования Swagger Petstore REST API на Python с использованием:

* `pytest` + `allure-pytest`  
* `requests`  
* `SQLAlchemy`  
* `jsonschema`

### Содержание

* [Описание проекта](#описание-проекта)  
* [Требования](#требования)  
* [Установка](#установка)  
* [Конфигурация](#конфигурация)  
* [Структура проекта](#структура-проекта)  
* [Запуск тестов](#запуск-тестов)  
* [CI / GitHub Actions](#ci--github-actions)  
* [Отчётность](#отчётность)  
* [Расширение и поддержка](#расширение-и-поддержка)  

### Описание проекта

Проект демонстрирует построение расширяемого REST-фреймворка с:

* **HTTP-клиентом** (`src/client.py`): методы `get`, `post`, `put`, `delete`, валидация JSON-ответов по схемам (`src/schemas/*.json`).  
* **Доступом к БД** (`src/db.py`): SQLAlchemy, фикстуры для инициализации схемы и синхронизации данных.  
* **Фабриками тестовых данных** (`tests/data.py`): `make_user()`, `make_order()`.  
* **Константами** (`tests/constants.py`): ключевые префиксы ответов (например, `LOGIN_SUCCESS_PREFIX`).  
* **Тестами** (`tests/`): позитивные и негативные сценарии для `/pet`, `/user`, `/store/order`.  
* **Allure** для генерации удобного HTML-отчёта.

### Требования

* Python 3.8+  
* Docker (Petstore API и Postgres)  
* Git  

### Установка

```bash
git clone https://github.com/RomanRyabinkin/petstore-rest-automation-python.git
cd petstore-rest-automation-python
python -m venv .venv
source .venv/bin/activate      # Linux/macOS
.\.venv\Scripts\Activate.ps1   # Windows PowerShell
pip install -r requirements.txt
```

### Конфигурация

```yaml
api:
  base_url: http://localhost:8080/api/v3
  timeout: 5

db:
  url: postgresql://test:test@localhost:5432/petstore
```

### Подготовка и запуск тестов

```bash
docker run -d --name petstore -p 8080:8080 swaggerapi/petstore3:unstable
docker run -d --name petstore-db   -e POSTGRES_USER=test -e POSTGRES_PASSWORD=test   -e POSTGRES_DB=petstore -p 5432:5432 postgres:15

pytest --maxfail=1 -q --cov=src --cov-report=xml --alluredir=allure-results
```

### CI и отчёты

CI настроен в `.github/workflows/ci.yml`, использует GitHub Actions для запуска тестов, загрузки отчётов в Codecov и Allure.

**Автор: Роман Рябинкин**


*Автор: Роман Рябинкин*
