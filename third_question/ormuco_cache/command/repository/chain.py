from .base import BaseRepository
from .memory import MemoryRepository
from .network import NetworkRepository

class ChainRepository(BaseRepository):
    def __init__(self, settings):
        super().__init__(settings) 
        self.memoryRepository = MemoryRepository(settings)
        self.networkRepository = NetworkRepository(settings)

    def retrieve(self, key):
        if self.memoryRepository.has_key(key):
            return self.memoryRepository.retrieve(key)
        return self.networkRepository.retrieve(key)
 
    def store(self, key, data):
        self.memoryRepository.store(key, data)
        self.networkRepository.store(key, data) 