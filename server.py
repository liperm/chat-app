from constants import *
from servers.server_factory import get_server
import sys

connection_type = sys.argv[1]

server = get_server(connection_type)

server.start()
