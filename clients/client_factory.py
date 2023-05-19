from constants import *
from clients import tcp_client, udp_client


def get_client(connection_type: str):
    if connection_type == "tcp":
        return tcp_client.Client(HOST, PORT)

    elif connection_type == "udp":
        return udp_client.Client(HOST, PORT)

    else:
        raise Exception("Invalid connection type. Must be: tcp, udp or quic")
