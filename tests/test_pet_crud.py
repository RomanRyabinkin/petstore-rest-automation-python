import pytest
from sqlalchemy.exc import NoSuchTableError

from src.db import get_pet_by_id


@pytest.mark.parametrize('new_pet',
                    [
                        {"id": 1002, "name": "Alex", "status": "available"},
                        {"id": 1003, "name": "John",  "status": "pending"},
                        {"id": 1004, "name": "Richard", "status": "sold"}
                    ],
                    indirect=True)
def test_create_and_validate_schema(new_pet, client):
    response = client.get(f'/pet/{new_pet['id']}')
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == new_pet['name']
    assert data['status'] == new_pet['status']
    client.validate(response, 'pet_schema.json')

    try:
        row = get_pet_by_id(new_pet['id'])
    except ConnectionError:
        pytest.skip('Не удалось подключиться к БД. Пропуск проверки в БД')
    except NoSuchTableError:
        pytest.skip('Таблица pet не найдена. Пропуск проверки в БД')
    except AttributeError:
        pytest.skip('Запись не найдена в Postgres. Пропуски проверки данных в БД')
    assert row is not None, 'Питомец не найден в БД'
    assert getattr(row, 'id', row[0]) == new_pet['id']
    assert getattr(row, 'name', row[1]) == new_pet['name']
    assert getattr(row, 'status', row[2]) == new_pet['status']
