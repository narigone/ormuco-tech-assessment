from .command import RetrieveCommand, StoreCommand

class OrmucoCacheClient:
    def __init__(self, settings):
        self.settings = settings
        self.retrieveCommand = RetrieveCommand(settings)
        self.storeCommand = StoreCommand(settings)

    def retrieve(self, key):
        return self.retrieveCommand.execute(key)

    def has_in_cache(self, key):
        data = self.retrieve(key)

        return data != None

    def store(self, key, data):
        return self.storeCommand.execute(key, data)
