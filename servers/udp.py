import socket
from datetime import datetime


class Server:
    def __init__(self, host, port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server.bind((host, port))
        print(f"Server listening on {port}")
        self.clients = []

    def start(self):
        while True:
            try:
                received_message = self.server.recvfrom(1024)
                client_addr = received_message[1]
                if client_addr not in self.clients:
                    self.server.sendto(b"Enter your nickname: ", client_addr)
                    nickname = self.server.recvfrom(2048)[0].decode("ascii")
                    self.clients.append(client_addr)
                    self.broadcast(
                        f"[server]: [{nickname} entered the chat]".encode("ascii")
                    )
                else:
                    message = received_message[0]
                    print(
                        f"Message arrived at {datetime.now()}: {message.decode('ascii')}"
                    )
                    formatted_message = f"[{datetime.now().time()}]" + message.decode(
                        "ascii"
                    )
                    self.broadcast(formatted_message.encode("ascii"))

            except Exception as e:
                print(e)
                return

    def broadcast(self, message):
        print(f"Message broadcasted at {datetime.now()}: {message}")
        for client in self.clients:
            self.server.sendto(message, client)
