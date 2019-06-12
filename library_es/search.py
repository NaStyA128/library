from api.base import es_library_api


results = es_library_api.users.get(query={"term": {"username": "florine.sharp"}})
results = es_library_api.users.get(query={"match_all": {}})
print(results)
