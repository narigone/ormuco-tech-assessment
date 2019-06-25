from .retrieve import RetrieveCommand
from .store import  StoreCommand

import json


class CommandParser:
    def __init__(self, settings):
        self.retrieveCommand = RetrieveCommand(settings)
        self.storeCommand = StoreCommand(settings)

    def parse(self, input):
        tokens = input.split(' ')
        command_token = tokens[0]
        key = tokens[1]
        if command_token == RetrieveCommand.COMMAND_PREFIX:
            return self.retrieveCommand.execute(key)
        elif command_token == StoreCommand.COMMAND_PREFIX:
            data = json.loads(tokens[2])
            return self.storeCommand.execute(key, data)
        else:
            raise Exception('invalid command')
