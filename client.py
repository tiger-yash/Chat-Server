from socket import *
from tkinter import *
from threading import *

hostIp = "127.0.0.1"
portNumber = 8888

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
clientSocket.connect((hostIp, portNumber))

# tkinter window
root = Tk()
root.title("Chat Server App : Apoorve shukla(20075014),Yash raj(20075098)")

window = Label(root,
               foreground="white",
               background="black",
               justify="center"
               )
window.pack(fill="x")

# all messages area
allMessages = Text(window, width=50, background="white")
allMessages.grid(row=0, column=0, padx=10, pady=10)

# Your message area
yourMessage = Entry(window, width=50)
yourMessage.insert(0, "Erase this and enter your message")
yourMessage.grid(row=1, column=0, padx=10, pady=10)


def sendMessageFunc():
    clientMessage = yourMessage.get()
    allMessages.insert(END, "\n" + "You- " + clientMessage)
    clientSocket.send(clientMessage.encode("utf-8"))


# Button to send message
btnSendMessage = Button(window, text="Send", width=20,
                        command=sendMessageFunc, bg="gray", cursor="hand2")
btnSendMessage.grid(row=2, column=0, padx=10, pady=10)


def recvMessageFunc():
    while True:
        serverMessage = clientSocket.recv(1024).decode("utf-8")
        print(serverMessage)
        allMessages.insert(END, "\n"+serverMessage)


recvThread = Thread(target=recvMessageFunc)
recvThread.daemon = True
recvThread.start()

window.mainloop()
