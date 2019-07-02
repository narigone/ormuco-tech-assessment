from ormuco_cache.command import RetrieveCommand, StoreCommand
from ormuco_cache.settings import OrmucoCacheClientSettings

class OrmucoCacheClient:
    def __init__(self, settings = None):
        self.settings = settings if settings else OrmucoCacheClientSettings()
        self.retrieveCommand = RetrieveCommand(self.settings)
        self.storeCommand = StoreCommand(self.settings)

    def retrieve(self, key):
        return self.retrieveCommand.execute(key)

    def store(self, key, data):
        return self.storeCommand.execute(key, data)
