import pytest
from src.client import ApiClient

client = ApiClient()


class TestPetNegative:
    @pytest.mark.parametrize('pet_id,expected_error', [
        (1045604060, True),  # Несуществующий ID объекта и ожидаемый код ответа
        ('abc', True)  # Невалидный ID объекта и ожидаемый код ответа
    ])
    def test_pet_get_invalid_id(self, pet_id, expected_error):
        response = client.get(f'/pet/{pet_id}')
        assert (response.status_code < 200 or response.status_code >= 300) == expected_error

    @pytest.mark.parametrize('payload', [
                                 {},  # пустой JSON
                                 {"name": "EmptyId"},  # JSON с пустым ID и ожидаемый код ответа
                             ])
    def test_post_pet_invalid_body(self, payload):
        response = client.post('/pet', json=payload)
        assert (response.status_code < 200 or response.status_code >= 300)

    @pytest.mark.parametrize('pet_id', [1045604060])
    def test_delete_nonexistent_pet(self, pet_id):
        response = client.delete(f'/pet/{pet_id}')
        # Удаление несуществующего объекта тут возвращает 200, а не 404 (идемпотентно)
        assert response.status_code == 200
