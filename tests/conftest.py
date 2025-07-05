# tests/conftest.py
import time

import pytest
from src.client import ApiClient


def pytest_addoption(parser):
    """
    Добавление опции --base-url для переопределения базового URL API.
    """
    parser.addoption(
        "--base-url",
        action="store",
        default=None,
        help="Base URL for the API (overrides config.yaml)"
    )


@pytest.fixture(scope="session", autouse=True)
def wait_for_api(client):
    """
    Ожидает готовности API перед запуском тестов.
    Выполняет GET-запрос к /pet/1 до 10 раз с задержкой 1 сек.
    При статусе < 500 считает сервис доступным.
    """
    for attempt in range(10):
        try:
            resp = client.get('/pet/1')
            print(f"[wait_for_api] Попытка {attempt+1}: GET {client._url('/pet/1')} -> {resp.status_code}")
            if resp.status_code < 500:
                return
        except Exception as e:
            print(f"[wait_for_api] Исключение: {e}")
        time.sleep(1)
    pytest.exit("Petstore API не ответил на /pet/1 после 10 секунд")


@pytest.fixture(scope="session")
def client(request):
    """
    Инициализация HTTP-клиента для тестов.
    Использует опцию --base-url, если она передана.
    """
    base_override = request.config.getoption("--base-url")
    client = ApiClient()
    if base_override:
        client.base = base_override.rstrip('/')
    return client


@pytest.fixture(scope="function")
def new_pet(client):
    """
    Создает нового питомца и после теста удаляет его.
    Возвращает словарь с данными питомца.
    """
    payload = {"id": 1001, "name": "TestPet", "status": "available"}
    resp = client.post("/pet", json=payload)
    assert resp.status_code == 200, f"Ошибка создания питомца: {resp.status_code} {resp.text}"
    yield payload
    del_resp = client.delete(f"/pet/{payload['id']}")
    assert del_resp.status_code == 200, f"Ошибка удаления питомца: {del_resp.status_code} {del_resp.text}"
