import allure
import requests


from data.handlers import Urls, Handlers
from data.user_data import User


@allure.suite('Авторизация пользователя')
class Testlogin:

    @allure.description("Успешная авторизация пользователя, который зарегистрирован в системе")
    @allure.title("Авторизация пользователя, который зарегистрирован в системе")
    def test_login_user(self):
        r = requests.post(f"{Urls.MAIN_URL}{Handlers.LOGIN}", json=User.data_correct)
        assert r.status_code == 200
        assert r.json().get('success') == True

    @allure.description("При авторизации пользователя с некорректным логином/паролем возникает ошибка")
    @allure.title("Авторизация с некорректным логином/паролем")
    def test_login_user_error(self):
        r = requests.post(f"{Urls.MAIN_URL}{Handlers.LOGIN}", json=User.data_negative)
        assert r.status_code == 401
        assert r.json().get('success') == False