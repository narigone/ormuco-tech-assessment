from ormuco_cache.command import RetrieveCommand, StoreCommand, CommandParser
from ormuco_cache.network import PeerProtocolFactory, ServerProtocolFactory
from ormuco_cache.settings import OrmucoCacheServerSettings

from twisted.internet import reactor, endpoints


class OrmucoCacheServer:
    def __init__(self, settings = None):
        self.settings = settings if settings else OrmucoCacheServerSettings()
        self.command_parser = CommandParser(self.settings)
        self.server_factory = ServerProtocolFactory(self.command_parser)
        self.peer_factory = PeerProtocolFactory(self.command_parser)

    def start_server(self):
        for peer in self.settings.peers:
            try:
                reactor.connectTCP(peer.host, peer.port, self.peer_factory)
            except:
                pass

        endpoints.serverFromString(
            reactor, "tcp:" + str(self.settings.listen_on)).listen(self.server_factory)
        reactor.run()

    def print_server_info(self):
        print("Server listening on port " + str(self.settings.listen_on))
        if len(self.settings.peers) > 0:
            print("Peers:")
            for peer in self.settings.peers:
                print(peer.host + ":" + str(peer.port))
