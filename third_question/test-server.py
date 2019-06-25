from ormuco_cache.server import OrmucoCacheServer
from ormuco_cache.settings import OrmucoCacheServerSettings

import time

settings = OrmucoCacheServerSettings()

cache_server = OrmucoCacheServer(settings)
print("Starting server on port " + str(settings.server.port))
cache_server.start_server()