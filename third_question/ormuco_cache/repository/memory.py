from collections import deque
from datetime import datetime

from ormuco_cache.repository.base import BaseRepository


class MemoryRepository(BaseRepository):
    def __init__(self, settings):
        super().__init__(settings)
        self.cached_items = deque()

    def retrieve(self, key):
        index = 0
        for item in self.cached_items:
            if item.key == key:
                cache_hit = item
                return self.handle_cache_hit(cache_hit, index)
            index = index + 1
        return None

    def handle_cache_hit(self, cache_hit, index):
        if cache_hit.expires < datetime.now():
            del self.cached_items[index]
            return None
        elif index > 0:
            del self.cached_items[index]
            if self.settings.cache_renew_on_hit:
                expiration_date = datetime.datetime.now() + datetime.timedelta(seconds=self.settings.cache_expiration)
                cache_hit.expires = expiration_date
            self.cached_items.appendleft(cache_hit)

        return cache_hit

    def store(self, cache_item):
        original_cached_item = self.retrieve(cache_item.key)
        if original_cached_item == None:
            self.cached_items.appendleft(cache_item)
        else:
            original_cached_item.data = cache_item.data
            original_cached_item.expires = cache_item.expires

        if len(self.cached_items) > self.settings.cache_max_size:
            self.cached_items.pop()

        return True
