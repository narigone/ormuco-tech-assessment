from .memory import MemoryRepository
from .chain import ChainRepository


class RepositoryFactory:
    memory_repository = None
    network_repository = None

    def get_memory_repository(settings):
        if RepositoryFactory.memory_repository == None:
            RepositoryFactory.memory_repository = MemoryRepository(settings)
        return RepositoryFactory.memory_repository

    def get_network_repository(settings):
        if RepositoryFactory.network_repository == None:
            RepositoryFactory.network_repository = ChainRepository(settings)
        return RepositoryFactory.network_repository

    def buildRepository(settings):
        if settings.server and not settings.is_server:
            return RepositoryFactory.get_network_repository(settings)
        else:
            return RepositoryFactory.get_memory_repository(settings)


