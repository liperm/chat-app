from constants import *
from servers import tcp, udp, quic


def get_server(connection_type: str):
    if connection_type == "tcp":
        return tcp.Server(HOST, PORT)

    elif connection_type == "udp":
        return udp.Server(HOST, PORT)

    elif connection_type == "quic":
        return quic.Server(HOST, PORT)

    else:
        raise Exception("Invalid connection type. Must be: tcp, udp or quic")
