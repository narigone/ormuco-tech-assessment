from ormuco_cache.repository.memory import MemoryRepository
from ormuco_cache.repository.chain import ChainClientRepository, ChainServerRepository


class RepositoryFactory:
    memory_repository = None
    client_network_repository = None
    server_network_repository = None


    def get_memory_repository(settings):
        if RepositoryFactory.memory_repository == None:
            RepositoryFactory.memory_repository = MemoryRepository(settings)
        return RepositoryFactory.memory_repository

    def get_client_network_repository(settings):
        if RepositoryFactory.client_network_repository == None:
            RepositoryFactory.client_network_repository = ChainClientRepository(settings)
        return RepositoryFactory.client_network_repository

    def get_server_network_repository(settings):
        if RepositoryFactory.server_network_repository == None:
            RepositoryFactory.server_network_repository = ChainServerRepository(settings)
        return RepositoryFactory.server_network_repository

    def get_client_repository(settings):
        if settings.server:
            return RepositoryFactory.get_client_network_repository(settings)
        else:
            return RepositoryFactory.get_memory_repository(settings)

    def get_server_repository(settings):
        if len(settings.peers) > 0:
            return RepositoryFactory.get_server_network_repository(settings)
        else:
            return RepositoryFactory.get_memory_repository(settings)

    def buildRepository(settings):
        if not settings.is_server:
            return RepositoryFactory.get_client_repository(settings)
        else:
            return RepositoryFactory.get_server_repository(settings)


