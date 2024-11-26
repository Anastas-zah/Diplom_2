import allure
import requests


from data.handlers import Urls, Handlers
from data.ingredients_data import Ingredient


@allure.suite("Создание заказа")
class TestCreateOrder:

    @allure.description("Тест на создание заказа с авторизацией")
    @allure.title("Создание заказа с валидным пользователем")
    def test_create_order(self, create_user):
        token = {'Authorization': create_user[3]}
        r = requests.post(f"{Urls.MAIN_URL}{Handlers.MAKE_ORDER}", headers=token, json=Ingredient.correct_ingredients_data)
        assert r.status_code == 200
        assert r.json().get("success") is True

    @allure.description("Тест на создание заказа без авторизации")
    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_authorization(self):
        r = requests.post(f"{Urls.MAIN_URL}{Handlers.MAKE_ORDER}", json=Ingredient.correct_ingredients_data)
        assert r.status_code == 200
        assert r.json().get("success") is True

    @allure.description("Тест на создание заказа без указания ингредиентов")
    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredient(self):
        r = requests.post(f"{Urls.MAIN_URL}{Handlers.MAKE_ORDER}")
        assert r.status_code == 400
        assert r.json()['message'] == 'Ingredient ids must be provided'

    @allure.description("Тест на создание заказа с некорректным хэшем ингредиента")
    @allure.title("Создание заказа с некорректными данными ингредиента")
    def test_create_order_invalid_hash_ingredient(self):
        response = requests.post(Urls.MAIN_URL + Handlers.MAKE_ORDER, headers=Handlers.headers, json=Ingredient.incorrect_ingredients_data)
        assert response.status_code == 500
        assert 'Internal Server Error' in response.text