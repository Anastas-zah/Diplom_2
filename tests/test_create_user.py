import pytest
import allure
import requests


from data.handlers import Urls, Handlers
from data.user_data import User


@allure.suite("Создание пользователя")
class TestCreateUser:

    @allure.description("Тест на создание нового пользователя")
    @allure.title("Создание нового пользователя")
    def test_create_new_user(self):
        r = requests.post(f"{Urls.MAIN_URL}{Handlers.CREATE_USER}", json=User.create_data_user())
        assert r.status_code == 200
        assert r.json()['success'] is True

    @allure.description("Тест на попытку создать существующего пользователя")
    @allure.title("Создание дублирующего пользователя")
    def test_create_double_user(self):
        r = requests.post(f"{Urls.MAIN_URL}{Handlers.CREATE_USER}", json=User.data_double)
        assert r.status_code == 403
        assert 'User already exists' in r.text

    @allure.description("Тест на создание пользователя с некорректными данными")
    @allure.title("Создание пользователя с некорректными данными")
    @pytest.mark.parametrize("user_data", [User.data_without_email, User.data_without_password, User.data_without_name])
    def test_create_user_incorrect_data(self, user_data):
        r = requests.post(f"{Urls.MAIN_URL}{Handlers.CREATE_USER}", json=user_data)
        assert r.status_code == 403
        assert 'Email, password and name are required fields' in r.text