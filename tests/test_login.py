import allure

from api_client import login_user
from data import (
    WRONG_EMAIL,
    WRONG_PASSWORD,
    INCORRECT_CREDENTIALS_MESSAGE
)


class TestUserLogin:

    @allure.title("Успешная авторизация существующего пользователя")
    def test_login_existing_user(self, registered_user):
        response = login_user(registered_user["data"])

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "accessToken" in response.json()
        assert "refreshToken" in response.json()

    @allure.title("Авторизация с неверным логином и паролем")
    def test_login_with_wrong_email_and_password(self, registered_user):
        user_data = registered_user["data"].copy()
        user_data["email"] = WRONG_EMAIL
        user_data["password"] = WRONG_PASSWORD

        response = login_user(user_data)

        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == (
            INCORRECT_CREDENTIALS_MESSAGE
        )