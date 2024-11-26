import allure
import requests

from data.handlers import Urls, Handlers
from data.user_data import User


@allure.suite('Изменение данных пользователя')
class TestChangingUserData:

    @allure.description("Успешное изменение данных при смене email у авторизованного пользователя")
    @allure.title("Изменение email пользователя")
    def test_changing_user_email(self, create_user):
        payload = {'email': User.create_data_user()["email"]}
        token = {'Authorization': create_user[3]}
        r = requests.patch(f"{Urls.MAIN_URL}{Handlers.CHANGE_USER_DATA}", headers=token, data=payload)
        assert r.status_code == 200
        assert r.json()['user']['email'] == payload["email"]

    @allure.description("Успешное изменение данных при смене пароля у авторизованного пользователя")
    @allure.title("Изменение пароля пользователя")
    def test_changing_user_password(self, create_user):
        payload = {'password': User.create_data_user()["password"]}
        token = {'Authorization': create_user[3]}
        r = requests.patch(f"{Urls.MAIN_URL}{Handlers.CHANGE_USER_DATA}", headers=token, data=payload)
        assert r.status_code == 200
        assert r.json().get("success") is True

    @allure.description("Успешное изменение данных при смене имени у авторизованного пользователя")
    @allure.title("Изменение имени пользователя")
    def test_changing_user_name(self, create_user):
        payload = {'name': User.create_data_user()["name"]}
        token = {'Authorization': create_user[3]}
        r = requests.patch(f"{Urls.MAIN_URL}{Handlers.CHANGE_USER_DATA}", headers=token, data=payload)
        assert r.status_code == 200
        assert r.json()['user']['name'] == payload["name"]

    @allure.description("Появление ошибки при смене данных пользователя без авторизации")
    @allure.title("Изменение данных пользователя без авторизации")
    def test_changing_user_data_without_authorization(self):
        r = requests.patch(f"{Urls.MAIN_URL}{Handlers.CHANGE_USER_DATA}", data=User.create_data_user())
        assert r.status_code == 401
        assert r.json()['message'] == 'You should be authorised'