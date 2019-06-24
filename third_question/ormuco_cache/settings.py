
class OrmucoSettings:
    def __init__(self):
        self.cache_max_size = 50
        self.cache_mem_size = 128 * 1024 * 1024
        self.cache_expiration = 60

        self.server = None
