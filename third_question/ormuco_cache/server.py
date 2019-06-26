from .command import RetrieveCommand, StoreCommand, CommandParser
from .network import PublishFactory

from twisted.internet import reactor, endpoints


class OrmucoCacheServer:
    def __init__(self, settings):
        self.settings = settings
        self.commandParser = CommandParser(settings)
        self.publishFactory = PublishFactory(self.commandParser)

    def start_server(self):
        endpoints.serverFromString(
            reactor, "tcp:" + str(self.settings.server.port)).listen(self.publishFactory)
        reactor.run()
