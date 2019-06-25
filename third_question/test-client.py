from ormuco_cache.client import OrmucoCacheClient
from ormuco_cache.settings import OrmucoCacheClientSettings

import time

settings = OrmucoCacheClientSettings()

cache_client = OrmucoCacheClient(settings)
key = "Teste" 

print("Is key " + key + " set: " +str(cache_client.has_in_cache(key)) )

cache_client.store(key, "teste")
print("Is key " + key + " set: " +str(cache_client.has_in_cache(key)) )
print(cache_client.retrieve(key))

time.sleep(settings.cache_expiration + 1)
print("Is key " + key + " set after sleep: " +str(cache_client.has_in_cache(key)) )
print(cache_client.retrieve(key))