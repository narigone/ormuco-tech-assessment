from .base import BaseRepository
from .memory import MemoryRepository
from .network import ClientNetworkRepository, ServerNetworkRepository


class ChainClientRepository(BaseRepository):
    def __init__(self, settings):
        super().__init__(settings)
        self.memory_repository = MemoryRepository(settings)
        self.network_repository = ClientNetworkRepository(settings)

    def retrieve(self, key):
        cache_item = self.memory_repository.retrieve(key)
        if cache_item != None:
            return cache_item

        cache_item = self.network_repository.retrieve(key)
        if cache_item != None:
            self.memory_repository.store(cache_item)

        return cache_item

    def store(self, cache_item):
        self.memory_repository.store(cache_item)
        self.network_repository.store(cache_item)
        return True


class ChainServerRepository(BaseRepository):
    def __init__(self, settings):
        super().__init__(settings)
        self.memory_repository = MemoryRepository(settings)
        self.network_repository = ServerNetworkRepository(settings)

    def retrieve(self, key):
        cache_item = self.memory_repository.retrieve(key)
        if cache_item != None:
            return cache_item
        return self.network_repository.retrieve(key)

    def store(self, cache_item):
        self.memory_repository.store(cache_item)
        self.network_repository.store(cache_item)
        return True
