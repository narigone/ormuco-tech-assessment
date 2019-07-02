from twisted.internet import protocol
from twisted.protocols import basic

import json

class ServerProtocol(basic.LineReceiver):
    def __init__(self, factory):
        self.factory = factory

    def connectionLost(self, reason):
        try:
            self.factory.peers.remove(self)
        except:
            pass

    def lineReceived(self, line):
        decoded_line = line.decode("utf-8")

        if decoded_line == "PEER":
            self.factory.peers.add(self)
            self.sendLine(b"ACK")
        else:
            result = self.factory.command_parser.parse(line.decode("utf-8"))
            self.send_response_to_emitter(result, self)

            # Propagate store command to peers
            if decoded_line.startswith('STR'):
                for peer in self.factory.peers:
                    if peer != self:
                        peer.sendLine(line)

    def send_response_to_emitter(self, result, client):
        try:
            if result == True:
                client.sendLine(b"ACK")
            elif result == None:
                client.sendLine(b"MISS")
            else:
                payload = json.dumps(result)
                client.sendLine(payload.encode())
        except:
            client.sendLine(b"NOOP")


class ServerProtocolFactory(protocol.Factory):
    def __init__(self, command_parser):
        self.peers = set()
        self.command_parser = command_parser

    def buildProtocol(self, addr):
        return ServerProtocol(self)
