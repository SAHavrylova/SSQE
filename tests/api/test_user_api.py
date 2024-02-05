import pytest


@pytest.mark.api
def test_create_user(petstore):
    user_data = {
        "id": 102030,
        "username": "SAw",
        "firstName": "Svitlana",
        "lastName": "Stest",
        "email": "new@new.com",
        "password": "NewSA123",
        "phone": "string",
        "userStatus": 0
    }

    response = petstore.create_user(user_data)

    assert response.status_code == 200
    assert response.json()["code"] == 200
    assert response.json()["type"] == "unknown"
    assert response.json()["message"] == str(user_data["id"])


@pytest.mark.api
def test_get_existing_user(petstore):
    existing_username = "SAw"

    response = petstore.get_user_by_username(existing_username)
    assert response.status_code == 200
    user_info = response.json()
    assert user_info["username"] == existing_username


@pytest.mark.api
def test_new_user_login(petstore):
    username = "SAw"
    password = "NewSA123"

    response = petstore.authenticate_user(username, password)
    assert response.status_code == 200
    assert "logged in user session" in response.json()["message"]


@pytest.mark.api
def test_update_user(petstore):
    username = "SAw"
    user_data = {
        "id": 10203040,
        "username": "SAw2",
        "firstName": "Svitlana",
        "lastName": "Stest",
        "email": "new@new.com",
        "password": "NewSA123",
        "phone": "string",
        "userStatus": 0
    }

    response = petstore.put_update_user(username, user_data)
    assert response.status_code == 200


@pytest.mark.api
def test_delete_user(petstore):
    username_delete = "SAw"

    response = petstore.delete_user_by_username(username_delete)
    assert response.status_code == 200




