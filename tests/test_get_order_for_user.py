import allure
import requests


from data.handlers import Urls, Handlers
from data.ingredients_data import Ingredient


@allure.suite("Тест на получение доступных заказов по пользователю")
class TestGetOrder:

    @allure.description("Тест на получение заказов для авторизованного пользователя")
    @allure.title("Получение заказов авторизованного пользователя")
    def test_get_order_user_with_authorization(self, create_user):
        token = {'Authorization': create_user[3]}
        requests_create_order = requests.post(f"{Urls.MAIN_URL}{Handlers.MAKE_ORDER}", headers=token, json=Ingredient.correct_ingredients_data)
        response_get_order = requests.get(f"{Urls.MAIN_URL}{Handlers.GET_ORDERS}", headers=token)
        assert response_get_order.status_code == 200
        assert response_get_order.json()['orders'][0]['number'] == requests_create_order.json()['order']['number']

    @allure.description("Тест на получение заказов для неавторизованного пользователя")
    @allure.title("Получение заказов без авторизации")
    def test_get_order_user_without_authorization(self):
        r = requests.get(f"{Urls.MAIN_URL}{Handlers.GET_ORDERS}")
        assert r.status_code == 401
        assert r.json()['message'] == 'You should be authorised'