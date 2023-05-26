import asyncio
from aioquic.quic.connection import QuicConnection
from aioquic.quic.configuration import QuicConfiguration
from aioquic.asyncio import serve


class ChatServer(asyncio.AbstractServer):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.configuration = QuicConfiguration(
            is_client=False,
            certificate="../certificate.pem",
            private_key="../private_key.pem",
        )
        self.server = QuicConnection(
            configuration=self.configuration,
            original_destination_connection_id=b"8e1bfc9061b0ebd49358385720a4ae158b75e1d5",
        )

    async def start(self):
        print("Starting Server...")
        server = await serve(
            self.host,
            self.port,
            configuration=self.configuration,
            create_protocol=self.server,
        )

        await asyncio.Future()


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def start(self):
        server = ChatServer(self.host, self.port)
        asyncio.run(server.start())
