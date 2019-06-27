from .command import RetrieveCommand, StoreCommand, CommandParser
from .network import PeerProtocolFactory, ServerProtocolFactory

from twisted.internet import reactor, endpoints


class OrmucoCacheServer:
    def __init__(self, settings):
        self.settings = settings
        self.commandParser = CommandParser(settings)
        self.serverFactory = ServerProtocolFactory(self.commandParser)
        self.peerFactory = PeerProtocolFactory(self.commandParser)

    def start_server(self):

        for peer in self.settings.peers:
            reactor.connectTCP(peer.host, peer.port, self.peerFactory)

        endpoints.serverFromString(
            reactor, "tcp:" + str(self.settings.server.port)).listen(self.serverFactory)
        reactor.run()
