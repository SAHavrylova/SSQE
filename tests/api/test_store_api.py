import pytest


@pytest.mark.api
def test_create_order(petstore):
    order_data = {
        "id": 7,
        "petId": 1107,
        "quantity": 0,
        "shipDate": "2024-02-05T19:18:49.685Z",
        "status": "placed",
        "complete": True
    }
    response = petstore.post_create_order(order_data)
    assert response.status_code == 200


@pytest.mark.api
def test_find_order(petstore):
    order_id = 7

    response = petstore.get_find_order(order_id)
    assert response.status_code == 200


@pytest.mark.api
def test_delete_order_by_id(petstore):
    order_id = 5

    response = petstore.delete_order(order_id)
    assert response.status_code == 200