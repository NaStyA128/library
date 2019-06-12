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

    def search(self, *args, **kwargs):
        return self.request('get', search=True, **kwargs)

    def get(self, *args, **kwargs):
        return self.request('get', **kwargs)

    def post(self, *args, **kwargs):
        return self.request('post', **kwargs)

    def put(self, *args, **kwargs):
        return self.request('put', **kwargs)

    def delete(self, *args, **kwargs):
        return self.request('delete', **kwargs)

    def request(self, method, *args, **kwargs):
        is_search = kwargs.pop('search')
        if is_search:
            return getattr(self.session, method)(self.get_search_url(),json=kwargs)

        detail_id = kwargs.pop(self.detail_field, None)
        return getattr(self.session, method)(self.get_doc_url(detail_id), json=kwargs)

    def get_doc_url(self, detail_id=None):
        return f'{self.base_api_url}{self.url}_doc/{detail_id}' if detail_id else f'{self.base_api_url}{self.url}_doc/'

    def get_search_url(self):
        return f'{self.base_api_url}{self.url}_search'


class UserIndex(BaseIndex):
    url = '/user/'


class PersonIndex(BaseIndex):
    url = '/person/'


class AuthorIndex(BaseIndex):
    url = '/author/'


class ESLibraryAPI:
    users = UserIndex()
    persons = PersonIndex()
    authors = AuthorIndex()


es_library_api = ESLibraryAPI()
