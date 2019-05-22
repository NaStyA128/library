import requests

from . import settings

# todo Will be later, need to think


class SingletoneSession(requests.Session):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance


class BaseIndex:
    url = None
    url_detail = None
    base_api_url = settings.ES_BASE_API_URL

    def __init__(self):
        self.session = SingletoneSession()

    def get(self, **kwargs):
        self.request('get', **kwargs)

    def post(self, **kwargs):
        self.request('post', **kwargs)

    def put(self, **kwargs):
        self.request('put', **kwargs)

    def delete(self, **kwargs):
        self.request('delete', **kwargs)

    def request(self, method, **params):
        detail_id = params.pop('detail_id', None)
        response = getattr(self.session, method)(method, self.get_url(detail_id), **params)
        return response

    def get_url(self, detail_id=None):
        return self.base_api_url.format(self.url_detail.format(detail_id) if detail_id else self.url)


class UserIndex(BaseIndex):
    url_detail = '/user/_doc/{}'


class ESLibraryAPI:
    users = UserIndex()


es_library_api = ESLibraryAPI()
