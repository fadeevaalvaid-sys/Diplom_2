import pytest

from api_client import create_user, delete_user
from data import USER_PASSWORD, USER_NAME
from helpers import generate_email


@pytest.fixture
def user_data():
    return {
        "email": generate_email(),
        "password": USER_PASSWORD,
        "name": USER_NAME
    }


@pytest.fixture
def registered_user(user_data):
    response = create_user(user_data)
    assert response.status_code == 200

    access_token = response.json()["accessToken"]

    yield {
        "data": user_data,
        "response": response,
        "access_token": access_token
    }

    delete_user(access_token)