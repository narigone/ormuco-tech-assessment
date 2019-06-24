from .repository import RepositoryFactory

class RetriveCommand:
    def __init__(self, settings): 
        self.repository = RepositoryFactory.buildRepository(settings)

    def execute(self, key):
        cache_item = self.repository.retrieve(key)
        if cache_item != None:
            return cache_item.data
        return None