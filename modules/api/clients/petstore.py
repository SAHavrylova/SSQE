import requests


class Petstore:
    
    def __init__(self, base_url = "https://petstore.swagger.io/v2"):
        self.base_url = base_url
    
    def create_user(self, user_data):
        endpoint = f"{self.base_url}/user"
        response = requests.post(endpoint, json=user_data)
        return response
    
    def get_user_by_username(self, username):
        endpoint = f"{self.base_url}/user/{username}"
        response = requests.get(endpoint)
        return response
