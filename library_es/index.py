import json

from api.base import es_library_api


def get_data(file_name: str):
    with open(file_name, 'r') as f:
        data = json.load(f)
        return data


class UserParser:
    data_file = '/home/user/learning/library/library_es/data_files/users.json'

    def parse(self):
        data = get_data(self.data_file)
        for item in data:
            es_library_api.users.put(**item)


if __name__ == '__main__':
    UserParser().parse()
