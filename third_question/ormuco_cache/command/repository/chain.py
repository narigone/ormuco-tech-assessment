from .base import BaseRepository
from .memory import MemoryRepository
from .network import NetworkRepository

class ChainRepository(BaseRepository):
    def __init__(self, settings):
        super().__init__(settings) 
        self.memoryRepository = MemoryRepository(settings)
        self.networkRepository = NetworkRepository(settings)

    def retrieve(self, key):
        cache_item = self.memoryRepository.retrieve(key)
        if cache_item != None:
            return cache_item
        return self.networkRepository.retrieve(key)
 
    def store(self, cache_item):
        self.memoryRepository.store(cache_item)
        self.networkRepository.store(cache_item) 