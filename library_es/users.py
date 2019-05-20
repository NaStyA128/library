from .api import es_library_api


def create_user(user_data):
    return es_library_api.users.post(username='some_username')


def get_user(user_id):
    return es_library_api.users.get(detail_id=user_id)
