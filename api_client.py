import requests
import allure

from urls import CREATE_USER, LOGIN_USER, CREATE_ORDER, DELETE_USER


@allure.step("Создание пользователя")
def create_user(user_data):
    return requests.post(CREATE_USER, json=user_data)


@allure.step("Авторизация пользователя")
def login_user(user_data):
    return requests.post(LOGIN_USER, json=user_data)


@allure.step("Создание заказа")
def create_order(ingredients, token=None):
    headers = {"Authorization": token} if token else {}
    return requests.post(
        CREATE_ORDER,
        json={"ingredients": ingredients},
        headers=headers
    )


@allure.step("Удаление пользователя")
def delete_user(token):
    return requests.delete(
        DELETE_USER,
        headers={"Authorization": token}
    )