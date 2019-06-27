from ormuco_cache.server import OrmucoCacheServer
from ormuco_cache.settings import OrmucoCacheServerSettings


settings = OrmucoCacheServerSettings()

cache_server = OrmucoCacheServer(settings)
cache_server.print_server_info()
cache_server.start_server()