import json

from api.base import es_library_api


def get_data(file_name: str):
    with open(file_name, 'r') as f:
        data = json.load(f)
        return data


class UserParser:
    data_file = '/home/user/Projects/learning/library/data_files/users.json'

    def parse(self):
        data = get_data(self.data_file)
        for item in data:
            es_library_api.users.put(**item)


class PersonParser:
    data_file = '/home/user/Projects/learning/library/data_files/persons.json'

    def parse(self):
        data = get_data(self.data_file)
        for item in data:
            es_library_api.persons.put(**item)


class AuthorParser:
    data_file = '/home/user/Projects/learning/library/data_files/authors.json'

    def parse(self):
        data = get_data(self.data_file)
        for item in data:
            es_library_api.authors.put(**item)


if __name__ == '__main__':
    # UserParser().parse()
    # PersonParser().parse()
    # AuthorParser().parse()
    pass
