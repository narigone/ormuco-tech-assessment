from ormuco_cache.client import OrmucoCacheClient
from ormuco_cache.settings import OrmucoCacheClientSettings

import time

settings = OrmucoCacheClientSettings()

cache_client = OrmucoCacheClient(settings)
key = "Chave"
data = [ 1, 2, 3] 
 
print("Is key " + key + " set: " +str(cache_client.has_in_cache(key)) )

cache_client.store(key, data) 
print("Is key " + key + " set: " +str(cache_client.has_in_cache(key)) )
print(cache_client.retrieve(key))