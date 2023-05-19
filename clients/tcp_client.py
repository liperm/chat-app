import socket
import threading


class Client:
    def __init__(self, host, port):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))
        self.nickname: str

    def write(self):
        while True:
            try:
                message = input()
                formated_message = "[{}]: {}".format(self.nickname, message)
                self.client.send(formated_message.encode("ascii"))
            except:
                raise Exception("Connection Lost!")

    def receive(self):
        while True:
            try:
                received_message = self.client.recv(2048).decode("ascii")
                print(received_message)
            except:
                raise Exception("An error has occured")

    def start(self):
        message = self.client.recv(1024).decode("ascii")

        self.nickname = input(message)
        self.client.send(self.nickname.encode("ascii"))

        print(self.client.recv(1024).decode("ascii"))

        write_thread = threading.Thread(target=self.write, args=())
        write_thread.start()

        receive_thread = threading.Thread(target=self.receive, args=())
        receive_thread.start()
