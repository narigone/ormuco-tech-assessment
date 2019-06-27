from twisted.internet.protocol import ReconnectingClientFactory
from twisted.protocols.basic import LineReceiver
from twisted.internet import protocol

class PeerProtocol(LineReceiver):
    def __init__(self, command_parser):
        self.command_parser = command_parser

    def connectionMade(self):
        self.sendLine(b"PEER")

    def lineReceived(self, line):
        decoded_line = line.decode("utf-8")
        if decoded_line != 'ACK':
            self.command_parser.parse(line.decode("utf-8"))


class PeerProtocolFactory(ReconnectingClientFactory):
    def __init__(self, command_parser):
        self.peers = set()
        self.command_parser = command_parser
 
    def buildProtocol(self, addr): 
        self.resetDelay()
        return PeerProtocol(self.command_parser)

    def clientConnectionLost(self, connector, reason):
        #print('Lost connection.  Reason:', reason)
        ReconnectingClientFactory.clientConnectionLost(self, connector, reason)

    def clientConnectionFailed(self, connector, reason):
        #print('Connection failed. Reason:', reason)
        ReconnectingClientFactory.clientConnectionFailed(self, connector, reason)
