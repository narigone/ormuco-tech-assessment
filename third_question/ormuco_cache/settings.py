import os

from dotenv import load_dotenv

load_dotenv()

class OrmucoServerSettings:
    def __init__(self, host, port):
        self.host = host
        self.port = port

class OrmucoCacheClientSettings:
    def __init__(self):
        self.cache_max_size = int(os.getenv('CACHE_MAX_SIZE')) if os.getenv('CACHE_MAX_SIZE') else 128
        self.cache_expiration = int(os.getenv('CACHE_EXPIRATION')) if os.getenv('CACHE_EXPIRATION') else 3600
        self.cache_renew_on_hit = True if os.getenv('CACHE_RENEW_ON_HIT') == 'True' else False 

        server_host = os.getenv('SERVER_HOST')
        server_port = int(os.getenv('SERVER_PORT'))
        if server_host and server_port:
            self.server = OrmucoServerSettings("localhost", 11142)
        
        self.is_server = False

class OrmucoCacheServerSettings(OrmucoCacheClientSettings):
    def __init__(self):
        super().__init__()
        self.listen_on = int(os.getenv('LISTEN_ON')) if os.getenv('LISTEN_ON') else 11142

        self.parse_peer_list()

        self.is_server = True

    def parse_peer_list(self):
        self.peers = set()
        peers_string = os.getenv('PEERS')
        if not peers_string:
            return

        for peer in peers_string.split(','):
            peer = peer.strip() 
            tokens = peer.split(':')

            peer_server = OrmucoServerSettings(tokens[0], int(tokens[1]))
            self.peers.add(peer_server)