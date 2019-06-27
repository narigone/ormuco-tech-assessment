from ormuco_cache.server import OrmucoCacheServer
from ormuco_cache.settings import OrmucoCacheServerSettings, OrmucoServerSettings
import time

settings = OrmucoCacheServerSettings()
settings.server.port = 11143

settings.peers.add(OrmucoServerSettings("localhost", 11142))

cache_server = OrmucoCacheServer(settings)
print("Starting server on port " + str(settings.server.port))
cache_server.start_server()
