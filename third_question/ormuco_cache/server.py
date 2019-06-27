from .command import RetrieveCommand, StoreCommand, CommandParser
from .network import PeerProtocolFactory, ServerProtocolFactory
from .settings import OrmucoCacheServerSettings

from twisted.internet import reactor, endpoints


class OrmucoCacheServer:
    def __init__(self, settings = None):
        self.settings = settings if settings else OrmucoCacheServerSettings()
        self.commandParser = CommandParser(self.settings)
        self.serverFactory = ServerProtocolFactory(self.commandParser)
        self.peerFactory = PeerProtocolFactory(self.commandParser)

    def start_server(self):
        for peer in self.settings.peers:
            try:
                reactor.connectTCP(peer.host, peer.port, self.peerFactory)
            except:
                pass

        endpoints.serverFromString(
            reactor, "tcp:" + str(self.settings.listen_on)).listen(self.serverFactory)
        reactor.run()

    def print_server_info(self):
        print("Server listening on port " + str(self.settings.listen_on))
        if len(self.settings.peers) > 0:
            print("Peers:")
            for peer in self.settings.peers:
                print(peer.host + ":" + str(peer.port))
