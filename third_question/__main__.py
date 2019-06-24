from ormuco_cache.client import OrmucoClient
from ormuco_cache.settings import OrmucoSettings

settings = OrmucoSettings()

cache_client = OrmucoClient(settings)
key = "Teste" 
print("Is key " + key + " set: " +str(cache_client.has_in_cache(key)) )
cache_client.store(key, "teste")
print("Is key " + key + " set: " +str(cache_client.has_in_cache(key)) )
print(cache_client.retrieve(key))