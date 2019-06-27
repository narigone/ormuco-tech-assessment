from .command import RetrieveCommand, StoreCommand
from .settings import OrmucoCacheClientSettings

class OrmucoCacheClient:
    def __init__(self, settings = None):
        self.settings = settings if settings else OrmucoCacheClientSettings()
        self.retrieveCommand = RetrieveCommand(self.settings)
        self.storeCommand = StoreCommand(self.settings)

    def retrieve(self, key):
        return self.retrieveCommand.execute(key)

    def has_in_cache(self, key):
        data = self.retrieve(key)

        return data != None

    def store(self, key, data):
        return self.storeCommand.execute(key, data)
