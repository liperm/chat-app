from constants import *
from servers import tcp


def get_server(connection_type: str):
    if connection_type == "tcp":
        return tcp.Server(HOST, PORT)
    else:
        raise Exception("Invalid connection type. Must be: tcp, udp or quic")
