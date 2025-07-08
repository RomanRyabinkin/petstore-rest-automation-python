import pytest
import allure
from src.client import ApiClient
from tests.constants import LOGIN_SUCCESS_PREFIX
from tests.data import make_user, make_order

client = ApiClient()

allure.feature('Раздел User')


class TestUserCRUD:

    @allure.story('Создание/Получение/Удаления пользователя')
    def test_create_get_delete_user(self):
        user = make_user()
        client.delete(f'/user/{user['username']}')
        response = client.post('/user', json=user)
        assert response.status_code == 200

        response = client.get(f'/user/{user['username']}')
        assert response.status_code == 200

        response = client.delete(f'/user/{user['username']}')
        assert response.status_code == 200

    @allure.story('Обновление пользователя (PUT запрос)')
    def test_update_user(self):
        newName = 'Roman123'
        user = make_user()
        client.post('/user', json=user)
        updated = make_user(
            firstName=newName,
            lastName='Ryabinkin123',
        )
        response = client.put(f'/user/{user["username"]}', json=updated)
        assert response.status_code == 200

        data = client.get(f'/user/{user["username"]}').json()
        assert data['firstName'] == newName

        client.delete(f'/user/{user['username']}')

    @allure.story('Авторизация и выход')
    def test_login_logout(self):
        user = make_user()
        client.post('/user', json=user)
        response = client.get(f"/user/login?username={user['username']}&password={user['password']}")
        assert response.status_code == 200
        assert LOGIN_SUCCESS_PREFIX in response.text
        response = client.get("/user/logout")
        assert response.status_code == 200

        client.delete(f"/user/{user['username']}")

    @allure.story('Создание массива юзеров')
    def test_create_with_array(self):
        user1 = make_user(id=6001, username='Rob')
        user2 = make_user(id=6002, username='Bob')
        response = client.post("/user/createWithArray", json=[user1, user2])
        assert response.status_code == 200

        client.delete(f"/user/{user1['username']}")
        client.delete(f"/user/{user2['username']}")



