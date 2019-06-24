from .base import BaseRepository

class NetworkRepository(BaseRepository):
    def __init__(self, settings):
        super().__init__(settings) 

    def has_key(self, key):
        pass

    def retrieve(self, key):
        pass
 
    def store(self, cache_item):
        pass