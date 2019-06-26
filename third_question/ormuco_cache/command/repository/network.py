import datetime
import json
import socket

from .. import *
from .base import BaseRepository

class NetworkRepository(BaseRepository):
    delimiter = b'\r\n'

    def __init__(self, settings):
        super().__init__(settings) 
 
    def send_command_to_server(self, command):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try: 
            sock.connect((self.settings.server.host, self.settings.server.port))
            sock.sendall(command.encode() + self.delimiter)
            response = b''

            while self.delimiter not in response:
                response += sock.recv(1024)

            response_as_string = response.decode('utf-8').strip() 
        except:
            return None
        finally:
            sock.close()

        return response_as_string

    def retrieve(self, key):
        command = "RTRV " + key

        json_data = self.send_command_to_server(command)

        if json_data == 'MISS':
            return None
        else:
            expiration_date = datetime.datetime.now() + datetime.timedelta(seconds=self.settings.cache_expiration)
            data = json.loads(json_data)
            cache_item = CacheItem(key, data, expiration_date) 
            return cache_item


    def store(self, cache_item):
        command = "STR " + cache_item.key + " " + json.dumps(cache_item.data)
        response = self.send_command_to_server(command)
        
        return response == 'ACK'
