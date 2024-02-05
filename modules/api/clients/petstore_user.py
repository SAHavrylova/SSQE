import requests


class Petstore:
    
    def __init__(self, base_url):
        self.base_url = base_url
    
    def create_user(self, user_data):
        endpoint = f"{self.base_url}/user"
        response = requests.post(endpoint, json=user_data)
        return response
    
    def get_user_by_username(self, username):
        endpoint = f"{self.base_url}/user/{username}"
        response = requests.get(endpoint)
        return response

    def authenticate_user(self, username, password):
        endpoint = f"{self.base_url}/user/login"
        params = {
            "username": username,
            "password": password
        }
        response = requests.get(endpoint, params=params)
        return response

    def put_update_user(self, username, user_data):
        endpoint = f"{self.base_url}/user/{username}"

        response = requests.put(endpoint, json=user_data)
        return response

    def delete_user_by_username(self, username):
        endpoint = f"{self.base_url}/user/{username}"
        response = requests.delete(endpoint)
        return response

    def add_new_pet(self, pet_data):
        endpoint = f"{self.base_url}/pet"
        response = requests.post(endpoint, json=pet_data)
        return response

    def find_pet_by_id(self, pet_id):
        endpoint = f"{self.base_url}/pet/{pet_id}"
        response = requests.get(endpoint)
        return response

    def