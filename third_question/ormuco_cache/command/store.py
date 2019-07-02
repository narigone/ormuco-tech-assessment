from ormuco_cache.repository import RepositoryFactory
from ormuco_cache.domain import CacheItemFactory


class StoreCommand:
    COMMAND_PREFIX = 'STR'

    def __init__(self, settings):
        self.settings = settings
        self.repository = RepositoryFactory.build_repository(settings)
        self.cache_item_factory = CacheItemFactory(self.settings)

    def execute(self, key, data):
        cache_item = self.cache_item_factory.build_cache_item(key, data)
        return self.repository.store(cache_item)
