from ormuco_cache.repository import RepositoryFactory

class RetrieveCommand:
    COMMAND_PREFIX = 'RTRV'

    def __init__(self, settings): 
        self.repository = RepositoryFactory.buildRepository(settings)

    def execute(self, key):
        cache_item = self.repository.retrieve(key)
        if cache_item != None:
            return cache_item.data
        return None