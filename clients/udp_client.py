import socket
import threading


class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.nickname: str

    def write(self):
        while True:
            try:
                message = input()
                formated_message = "[{}]: {}".format(self.nickname, message)
                self.client.sendto(
                    formated_message.encode("ascii"), (self.host, self.port)
                )
            except:
                raise Exception("Connection Lost!")

    def receive(self):
        while True:
            try:
                received_message = self.client.recvfrom(2048)[0].decode("ascii")
                print(received_message)
            except:
                raise Exception("An error has occured")

    def start(self):
        self.client.sendto(b"CONNECT", (self.host, self.port))
        message = self.client.recvfrom(1024)[0].decode("ascii")

        self.nickname = input(message)
        self.client.sendto(self.nickname.encode("ascii"), (self.host, self.port))

        print(self.client.recvfrom(1024)[0].decode("ascii"))

        write_thread = threading.Thread(target=self.write, args=())
        write_thread.start()

        receive_thread = threading.Thread(target=self.receive, args=())
        receive_thread.start()
