import requests

ES_BASE_API_URL = 'http://localhost:9200'


def get_user(user_id: str):
    user_url = f'/user/_doc/{user_id}'
    return requests.get(f'{ES_BASE_API_URL}{user_url}')


def create_or_update_user(user_id: str, user_data: dict):
    user_url = f'/user/_doc/{user_id}'
    return requests.put(f'{ES_BASE_API_URL}{user_url}', json=user_data)


def delete_user(user_id: str):
    user_url = f'/user/_doc/{user_id}'
    return requests.delete(f'{ES_BASE_API_URL}{user_url}')
