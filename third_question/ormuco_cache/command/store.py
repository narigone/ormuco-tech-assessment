import datetime

from .repository import RepositoryFactory
from .domain import CacheItem

class StoreCommand:
    COMMAND_PREFIX = 'STR'

    def __init__(self, settings): 
        self.settings = settings
        self.repository = RepositoryFactory.buildRepository(settings)

    def execute(self, key, data, with_dispatch = True):
        expiration_date = datetime.datetime.now() + datetime.timedelta(seconds=self.settings.cache_expiration)
        cache_item = CacheItem(key, data, expiration_date)
        return self.repository.store(cache_item)