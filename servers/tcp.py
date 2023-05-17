import socket
import threading


class Server:
    def __init__(self, host, port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))

        self.server.listen()

        self.clients = []

    def start(self):
        while True:
            try:
                client, addr = self.server.accept()

                client_thread = threading.Thread(
                    target=self.handle_client, args=(client, addr)
                )
                client_thread.start()
            except Exception as e:
                print(e)

    def handle_client(self, client, addr):
        client.send(b"Enter your nickname: ")
        nickname = client.recv(1024).decode("ascii")
        self.clients.append(client)

        print(f"Client [{nickname}] connected with address {addr}")
        self.broadcast(f"{nickname} connected to the server! Welcome".encode("ascii"))

        while True:
            try:
                message = client.recv(2048)
                self.broadcast(message)
            except Exception as e:
                print(e)
                index = self.clients.index(client)
                self.clients.remove(client)
                client.close()
                break

    def broadcast(self, message):
        for client in self.clients:
            client.send(message)
