# Ormuco Cache Library

This project is a cache library, loosely-based on memcached. It stores key/value pairs in memory for fast access. Can be used as a stand-alone cache as well as in a client/server model. Servers can be inter-connected, allowing information to be easily shared.

## Installation

Download the code and install its dependencies:
```
pip install -r requirements.txt
```

## Using the client library

The client library was created with simplicity in mind. It has two methods:
* **store** which takes two arguments: **key** - a string identifier for the data to be stored and **data** - the variable to be stored
* **retrieve** that takes as single argument: **key** - a string identifier for the data to be retrieved

```
from ormuco_cache.client import OrmucoCacheClient

cache_client = OrmucoCacheClient()
# Key can be any valid string
key = "my-key"

# Data can be any valid variable
data = [1, 2, 3]

# Use this method to store the data 
cache_client.store(key, data)

# Retrieves data
cache_client.retrieve(key)
```

## Starting a server

While the stand-alone version can be useful to save time by avoiding repeated computationon, all data is lost once the process is over. In order to persist data, it must be stored in a server node, which can be started by this command:

```
$ python start-server.py
Server listens on port 11142
```

It can also be done programatically:

```
from ormuco_cache.server import OrmucoCacheServer

cache_server = OrmucoCacheServer()
cache_server.start_server()
```

## Configuration

If you want to change some of the behaviour of the cache library, you must copy the __.env.example__ file to __.env__ and alter one the following

```
# Size of LRU cache set
CACHE_MAX_SIZE=128

# Time in seconds after which a cache item is deemed expired
CACHE_EXPIRATION=3600

# Determines whether the cache item's expiration is reset when a client requests it
CACHE_RENEW_ON_HIT=True

# Client-only configuration: designates server host and port for connection. Leave it blank for stand-alone in-memory caching
SERVER_HOST=localhost
SERVER_PORT=11142

# Server-only configuration: assign which port it will listen on
LISTEN_ON=11142

# Server-only configuration: comma separated peer list, using host:port format
PEERS=peer1:11142,peer2:11142
```

## Backlog

This project was created as a proof of concept. It still requires a few features before it is production ready:
* **Authentication**: As is, all connections are accepted. Coming up with an authentication architecture is necessary.
* **Network Encryption**: Right now, all connections are unecrypted over TCP/IP. Will study how to integrate with Let's Encrypt and other SSL/TLS authorities.
* **Packaging**: Need to publish it on PyPi, to make it easier to use.

## Authors

* **Raphael Sales** - [narigone](https://github.com/narigone)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
 