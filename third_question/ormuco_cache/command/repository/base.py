from abc import ABC, abstractmethod


class BaseRepository(ABC):
    def __init__(self, settings):
        self.settings = settings
        super().__init__()

    @abstractmethod
    def retrieve(self, key):
        pass

    @abstractmethod
    def store(self, cache_item):
        pass
