import pytest

from src.client import ApiClient


def pytest_adoption(parser):
    parser.addoption(
        '--base_url',
        action='store',
        default=None,
        help='Базовый URL для API'
    )


@pytest.fixture(scope='session')
def client(request):
    base_override = request.config.getoption('--base_url')
    client = ApiClient()
    if base_override:
        client.base = base_override.rstrip('/')
    return client


@pytest.fixture(scope='function')
def new_pet(client):
    """
    Создание нового объекта питомца перед тестом и его удаление после теста.

    Вовзаращает словарь с данными питомца.
    """
    payload = {
        'id': 1001,
        'name': 'TestPet',
        'status': 'available'
    }
    response = client.post('/pet', json=payload)
    assert response.status_code == 200, f'Ошибка создания питомца: {response.text}'

    yield payload
    deleted_response = client.delete(f'/pet/{payload["id"]}')
    assert deleted_response.status_code == 200, f'Ошибка удаления питомца: {deleted_response.text}'
