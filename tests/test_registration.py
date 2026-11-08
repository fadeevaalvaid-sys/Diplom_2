import allure

from api_client import create_user
from data import (
    USER_ALREADY_EXISTS_MESSAGE,
    REQUIRED_FIELDS_MESSAGE
)


class TestUserRegistration:

    @allure.title("Успешное создание уникального пользователя")
    def test_create_unique_user(self, registered_user):
        response = registered_user["response"]

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание уже зарегистрированного пользователя")
    def test_create_existing_user(self, registered_user):
        response = create_user(registered_user["data"])

        assert response.status_code == 403
        assert response.json()["message"] == USER_ALREADY_EXISTS_MESSAGE

    @allure.title("Создание пользователя без обязательного поля")
    def test_create_user_without_name(self, user_data):
        user_data.pop("name")
        response = create_user(user_data)

        assert response.status_code == 403
        assert response.json()["message"] == REQUIRED_FIELDS_MESSAGE