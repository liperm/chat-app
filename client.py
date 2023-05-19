import sys
from clients.client_factory import get_client

connection_type = sys.argv[1]

client = get_client(connection_type)

client.start()
