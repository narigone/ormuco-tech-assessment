import time
import unittest

from ormuco_cache.domain import CacheItem, CacheItemFactory
from ormuco_cache.settings import OrmucoCacheClientSettings, OrmucoCacheServerSettings, OrmucoServerSettings
from ormuco_cache.repository import RepositoryFactory
from ormuco_cache.repository.chain import ChainClientRepository, ChainServerRepository
from ormuco_cache.repository.memory import MemoryRepository
from ormuco_cache.repository.network import ClientNetworkRepository


class TestRepositoryFactory(unittest.TestCase):
    def test_client_chain_repository_creation(self):
        settings = OrmucoCacheClientSettings()
        repository = RepositoryFactory.build_repository(settings)

        self.assertIsInstance(repository, ChainClientRepository)

    def test_client_memory_repository_creation(self):
        settings = OrmucoCacheClientSettings()
        settings.server = None

        repository = RepositoryFactory.build_repository(settings)

        self.assertIsInstance(repository, MemoryRepository)

    def test_server_chain_repository_creation(self):
        settings = OrmucoCacheServerSettings()
        settings.peers.add(OrmucoServerSettings("localhost", 11142))

        repository = RepositoryFactory.build_repository(settings)

        self.assertIsInstance(repository, ChainServerRepository)

    def test_server_memory_repository_creation(self):
        settings = OrmucoCacheServerSettings()
        repository = RepositoryFactory.build_repository(settings)

        self.assertIsInstance(repository, MemoryRepository)


class TestMemoryRepository(unittest.TestCase):
    def test_unset_key_returns_none(self):
        settings = OrmucoCacheClientSettings()
        repository = MemoryRepository(settings)

        result = repository.retrieve('unset-key')

        self.assertEqual(result, None)

    def test_set_key_returns_same_data(self):
        settings = OrmucoCacheClientSettings()
        repository = MemoryRepository(settings)
        factory = CacheItemFactory(settings)

        key = 'some-key'
        data = [1, 2, 3]
        cache_item = factory.build_cache_item(key, data)

        store_result = repository.store(cache_item)
        self.assertEqual(store_result, True)

        retrieve_result = repository.retrieve(key)
        self.assertEqual(retrieve_result, cache_item)

    def test_data_overwrite(self):
        settings = OrmucoCacheClientSettings()
        repository = MemoryRepository(settings)
        factory = CacheItemFactory(settings)

        key = 'some-key'
        data = [1, 2, 3]
        cache_item = factory.build_cache_item(key, data)

        store_result = repository.store(cache_item)
        self.assertEqual(store_result, True)
        data = [1, 2, 3, 4]
        cache_item = factory.build_cache_item(key, data)

        store_result = repository.store(cache_item)
        self.assertEqual(store_result, True)

        retrieve_result = repository.retrieve(key)
        self.assertEqual(retrieve_result.data, data)

    def test_lru_cache_updating(self):
        settings = OrmucoCacheClientSettings()
        repository = MemoryRepository(settings)
        factory = CacheItemFactory(settings)

        for i in range(0, 3):
            key = str(i + 1)
            data = [1, 2, 3]
            cache_item = factory.build_cache_item(key, data)
            repository.store(cache_item) 

        retrieve_result = repository.retrieve(str(1))
        self.assertIsInstance(retrieve_result, CacheItem)

    def test_overflow_cache_size(self):
        settings = OrmucoCacheClientSettings()
        repository = MemoryRepository(settings)
        factory = CacheItemFactory(settings)

        for i in range(0, settings.cache_max_size + 2):
            key = str(i + 1)
            data = [1, 2, 3]
            cache_item = factory.build_cache_item(key, data)
            repository.store(cache_item) 

        retrieve_result = repository.retrieve(str(5))
        self.assertIsInstance(retrieve_result, CacheItem)

    def test_cache_item_expiration(self):
        settings = OrmucoCacheClientSettings()
        settings.cache_expiration = 0.0001
        repository = MemoryRepository(settings)
        factory = CacheItemFactory(settings)

        key = 'some-key'
        data = [1, 2, 3]
        cache_item = factory.build_cache_item(key, data)

        store_result = repository.store(cache_item)
        self.assertEqual(store_result, True)

        time.sleep(settings.cache_expiration)
        retrieve_result = repository.retrieve(key)
        self.assertEqual(retrieve_result, None)

class TestNetworkRepository(unittest.TestCase):
    def test_unset_key_returns_none(self):
        settings = OrmucoCacheClientSettings()
        repository = ClientNetworkRepository(settings)

        result = repository.retrieve('unset-key')

        self.assertEqual(result, None)

    def test_set_key_returns_same_data(self):
        settings = OrmucoCacheClientSettings()
        repository = ClientNetworkRepository(settings)
        factory = CacheItemFactory(settings)

        key = 'some-key'
        data = [1, 2, 3]
        cache_item = factory.build_cache_item(key, data)

        store_result = repository.store(cache_item)
        self.assertEqual(store_result, True)

        retrieve_result = repository.retrieve(key)
        self.assertEqual(retrieve_result.data, data)

    def test_retrieve_from_invalid_server(self):
        settings = OrmucoCacheClientSettings()
        settings.server.port = 12424

        repository = ClientNetworkRepository(settings)
        factory = CacheItemFactory(settings)

        key = 'some-key'

        retrieve_result = repository.retrieve(key)
        self.assertEqual(retrieve_result, None)

    def test_store_to_invalid_server(self):
        settings = OrmucoCacheClientSettings()
        settings.server.port = 12424

        repository = ClientNetworkRepository(settings)
        factory = CacheItemFactory(settings)

        key = 'some-key'
        data = [1, 2, 3]
        cache_item = factory.build_cache_item(key, data)

        store_result = repository.store(cache_item)
        self.assertEqual(store_result, False)
