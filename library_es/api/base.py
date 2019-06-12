import requests


class SingletonSession(requests.Session):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance


class BaseIndex:
    url = None
    detail_field = 'id'
    base_api_url = 'http://localhost:9200'

    def __init__(self):
        self.session = SingletonSession()

    def get(self, *args, **kwargs):
        return self.request('get', **kwargs)

    def post(self, *args, **kwargs):
        return self.request('post', **kwargs)

    def put(self, *args, **kwargs):
        return self.request('put', **kwargs)

    def delete(self, *args, **kwargs):
        return self.request('delete', **kwargs)

    def request(self, method, *args, **kwargs):
        detail_id = kwargs.pop(self.detail_field, None)
        print(detail_id)
        print(self.get_url(detail_id))
        print(kwargs)
        return getattr(self.session, method)(self.get_url(detail_id), json=kwargs, data=kwargs)

    def get_url(self, detail_id=None):
        return f'{self.base_api_url}{self.url}{detail_id}' if detail_id else f'{self.base_api_url}{self.url}'


class UserIndex(BaseIndex):
    url = '/user/_doc/'


class PersonIndex(BaseIndex):
    url = '/person/_doc/'


class AuthorIndex(BaseIndex):
    url = '/author/_doc/'


class ESLibraryAPI:
    users = UserIndex()
    persons = PersonIndex()
    authors = AuthorIndex()


es_library_api = ESLibraryAPI()
