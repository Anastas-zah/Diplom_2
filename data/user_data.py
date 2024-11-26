from faker import Faker


class User:

    @staticmethod
    def create_data_user():
        fake = Faker()

        reg_data = {
            "email": fake.email(),
            "password": fake.password(),
            "name": fake.name()}
        return reg_data

    data_correct = {
        "email": 'test_2011@yandex.ru',
        "password": "password"}

    data_negative = {
        "email": 'test20112024@yandex.ru',
        "password": "password"}

    data_double = {
        "email": 'test_2011@yandex.ru',
        "password": "password",
        "name": "Username"}

    data_without_email = {
        "email": '',
        "password": "password",
        "name": "Username"}

    data_without_password = {
        "email": 'test_2011@yandex.ru',
        "password": "",
        "name": "Username"}

    data_without_name = {
        "email": 'test_2011@yandex.ru',
        "password": "password",
        "name": ""}

    data_updated = {
        "email": 'test_2011@yandex.ru',
        "password": "password",
        "name": "Test"}