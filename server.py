from socket import *
from threading import *

hostIpAdd = "127.0.0.1"
port = 8888

hostSocket = socket(AF_INET, SOCK_STREAM)
hostSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

hostSocket.bind((hostIpAdd, port))
hostSocket.listen()
print("Connection is ready waiting for clients....")

clients = set()

def clientSideHandle(clientSocket, clientAddress):
    while True:
        message = clientSocket.recv(1024).decode("utf-8")
        for client in clients:
            if client is not clientSocket:
                client.send(
                    (clientAddress[0] + ":" + str(clientAddress[1]) + " says- " + message).encode("utf-8"))

        if not message:
            clients.remove(clientSocket)
            print(clientAddress[0] + ":" +
                  str(clientAddress[1]) + " client disconnected")
            break

    clientSocket.close()


while True:
    clientSocket, clientAddress = hostSocket.accept()
    clients.add(clientSocket)
    print("Connected with: ", clientAddress[0] + ":" + str(clientAddress[1]))
    thread = Thread(target=clientSideHandle, args=(clientSocket, clientAddress, ))
    thread.start()
