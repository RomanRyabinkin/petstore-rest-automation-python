import pytest, allure

from tests.constants import LOGGED_IN_USER_SESSION
from tests.data import make_user
from src.client import ApiClient

client = ApiClient()


class TestUserNegative:

    @allure.story('Негативный кейс: получение пользователя с несуществующим username')
    @pytest.mark.parametrize("username, code", [
        ('nosuchuser', 500),  #Не существующий пользователь
        ('', 405),  # Пустое имя
    ])
    def test_get_user_incvalid(self, username, code):
        r = client.get(f"/user/{username}")
        assert r.status_code == code

    @allure.story('Негативный кейс: создание пользователя с не валидным payload')
    @pytest.mark.parametrize('payload', [
        {},
        {'username': 'test'}
    ])
    def test_create_user_invalid_payload(self, payload):
        response = client.post('/user', json=payload)
        assert 400 <= response.status_code < 600

    @allure.story('Негативный кейс: Авторизация с некорректными данными')
    @pytest.mark.parametrize('q', [
        '?username=nosuch&password=123',
        '?username=&password=',
    ])
    def test_login_invalid(self, q):
        # Swagger Petstore возвращает 200
        response = client.get(f"/user/login{q}")
        assert response.status_code == 200
        assert LOGGED_IN_USER_SESSION not in response.text

    def test_update_nonexistent_user(self):
        response = client.put('/user/nobody', json=make_user())
        assert response.status_code == 500

