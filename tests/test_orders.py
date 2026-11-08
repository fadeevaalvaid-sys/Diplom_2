import allure

from api_client import create_order
from data import (
    VALID_INGREDIENTS,
    INVALID_INGREDIENT,
    EMPTY_INGREDIENTS_MESSAGE,
    INVALID_INGREDIENT_MESSAGE
)


class TestCreateOrder:

    @allure.title("Создание заказа авторизованным пользователем")
    def test_create_order_with_auth(self, registered_user):
        response = create_order(
            VALID_INGREDIENTS,
            registered_user["access_token"]
        )

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "number" in response.json()["order"]

    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_auth(self):
        response = create_order(VALID_INGREDIENTS)

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "number" in response.json()["order"]

    @allure.title("Создание заказа с ингредиентами")
    def test_create_order_with_ingredients(self, registered_user):
        response = create_order(
            [VALID_INGREDIENTS[0]],
            registered_user["access_token"]
        )

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "number" in response.json()["order"]

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self):
        response = create_order([])

        assert response.status_code == 400
        assert response.json()["success"] is False
        assert response.json()["message"] == EMPTY_INGREDIENTS_MESSAGE

    @allure.title("Создание заказа с неверным хешем ингредиента")
    def test_create_order_with_invalid_ingredient(self):
        response = create_order([INVALID_INGREDIENT])

        assert response.status_code == 400
        assert response.json()["success"] is False
        assert response.json()["message"] == INVALID_INGREDIENT_MESSAGE