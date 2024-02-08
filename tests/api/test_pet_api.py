import pytest


# what else except status code could be verified?
# in real project try your best to not use hardcoded ids, cause it could lead to unstable and dependent tests
@pytest.mark.api
def test_add_a_few_pets(petstore):
    # just for a future :)
    # it will be better to make some method like get_new_pet_data(name, category, pthoto, tags, status) where all structure will be covered
    # For long and variable structures pattern Builder could be used
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

# understandable that it's can not be done with this test endpoint
# but for the future it's bad approach to use hardcoded Ids in tests, in case of different envs or some side changes in DB
@pytest.mark.api
def test_find_pet_by_id(petstore):
    id_pet = 2396
    response = petstore.get_find_pet_by_id(id_pet)

    assert response.status_code == 200


@pytest.mark.api
def test_update_pet(petstore):
    pet_data = {
        "id": 2394,
        "category": {
            "id": 2396,
            "name": "string"
        },
        "name": "ToToSha",
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

    response = petstore.put_update_pet(pet_data)
    assert response.status_code == 200
