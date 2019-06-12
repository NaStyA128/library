from api.base import es_library_api


results = es_library_api.users.search(query={"term": {"username": "florine.sharp"}})
# results = es_library_api.users.search(query={"match_all": {}})
print(results.content)
