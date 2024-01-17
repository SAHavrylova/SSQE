import pytest

@pytest.mark.api
def test_create_user(petstore):
    user_data = {
        "id": 1,
        "username": "SA",
        "firstName": "Svitlana",
        "lastName": "Stest",
        "email": "new@new.com",
        "password": "string",
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
    existing_username = "user1"

    response = petstore.get_user_by_username(existing_username)
    assert response.status_code == 200
    user_info = response.json()
    assert user_info["username"] == existing_username



