from twisted.internet import protocol
from twisted.protocols import basic

import json


class PublishProtocol(basic.LineReceiver):
    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        self.factory.clients.add(self)

    def connectionLost(self, reason):
        self.factory.clients.remove(self)

    def lineReceived(self, line): 
        result = self.factory.commandParser.parse(line.decode("utf-8") )

        for c in self.factory.clients:
            if result == True:
                c.sendLine(b"ACK")
            elif result == None:
                c.sendLine(b"MISS")
            else:
                payload = "DATA " + json.dumps(result)
                c.sendLine(payload.encode())

class PublishFactory(protocol.Factory):
    def __init__(self, commandParser):
        self.clients = set()
        self.commandParser = commandParser

    def buildProtocol(self, addr):
        return PublishProtocol(self)
