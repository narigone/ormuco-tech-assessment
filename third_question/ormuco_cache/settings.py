class OrmucoServerSettings:
    def __init__(self, host, port):
        self.host = host
        self.port = port

class OrmucoCacheClientSettings:
    def __init__(self):
        self.cache_max_size = 128
        self.cache_mem_size = 128 * 1024 * 1024
        self.cache_expiration = 60

        self.server = OrmucoServerSettings("localhost", 11142)

class OrmucoCacheServerSettings:
    def __init__(self):
        self.cache_max_size = 128
        self.cache_mem_size = 128 * 1024 * 1024
        self.cache_expiration = 60

        self.server = OrmucoServerSettings("localhost", 11142)