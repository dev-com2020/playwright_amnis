import requests

def get_user_data(user_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    if response.status_code == 200:
        return response.json()
    return None