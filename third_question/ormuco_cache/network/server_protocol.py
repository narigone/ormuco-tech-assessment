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
        decoded_line = line.decode("utf-8")
        result = self.factory.command_parser.parse(line.decode("utf-8"))

        for client in self.factory.clients:
            if self.is_client_sender(client, self.transport):
                self.send_response_to_emitter(result, client)
            elif decoded_line.startswith('STR'):
                client.sendLine(line)

    def is_client_sender(self, client, sender):
        return client.transport.repstr == sender.repstr

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
            client.sendLine(b"NOP")


class PublishFactory(protocol.Factory):
    def __init__(self, command_parser):
        self.clients = set()
        self.command_parser = command_parser

    def buildProtocol(self, addr):
        return PublishProtocol(self)
