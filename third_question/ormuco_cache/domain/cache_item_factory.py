import datetime
import json

from . import CacheItem

class CacheItemFactory:

    def __init__(self, settings):
        self.settings = settings

    def build_cache_item(self, key, data):
        expiration_date = datetime.datetime.now() + datetime.timedelta(seconds=self.settings.cache_expiration)
        return CacheItem(key, data, expiration_date)

    def restore_cache_item(self, key, json_data):
        expiration_date = datetime.datetime.now() + datetime.timedelta(seconds=self.settings.cache_expiration)
        data = json.loads(json_data)
        return CacheItem(key, data, expiration_date) 