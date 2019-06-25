from .base import BaseRepository

class NetworkRepository(BaseRepository):
    def __init__(self, settings):
        super().__init__(settings) 

    def retrieve(self, key):
        pass
 
    def store(self, cache_item):
        pass