import pytest


@pytest.mark.api
def test_add_a_few_pets(petstore):
    pet_data_list = [
        {
            "id": 2395,
            "category": {
                "id": 2395,
                "name": "string"
            },
            "name": "Sonya",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 2395,
                    "name": "string"
                }
            ],
            "status": "available"
        },
        {
            "id": 2396,
            "category": {
                "id": 2396,
                "name": "string"
            },
            "name": "ToTo",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 2396,
                    "name": "string"
                }
            ],
            "status": "available"
        }
    ]

    for pet_data in pet_data_list:
        response = petstore.add_new_pet(pet_data)
        assert response.status_code == 200

@pytest.mark.api
def test_find_pet_by_id(petstore):
    id_pet = 2396
    response = petstore.find_pet_by_ids(id_pet)

    assert response.status_code == 200

