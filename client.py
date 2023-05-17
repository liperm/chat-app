import signal
import socket
import threading
from constants import *


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

message = client.recv(1024).decode("ascii")
nickname = input(message)
client.send(nickname.encode("ascii"))

print(client.recv(1024).decode("ascii"))


def write():
    while True:
        try:
            message = input()
            formated_message = "[{}]: {}".format(nickname, message)
            client.send(formated_message.encode("ascii"))
        except:
            raise Exception("Connection Lost!")


def receive():
    while True:
        try:
            received_message = client.recv(2048).decode("ascii")
            print(received_message)
        except:
            raise Exception("An error has occured")


write_thread = threading.Thread(target=write, args=())
write_thread.start()

receive_thread = threading.Thread(target=receive, args=())
receive_thread.start()
