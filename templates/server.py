from socket import socket
from telnetlib import Telnet
from time import sleep

# Create a socket, used for sending + receiving
sock = socket()
#             URL, port
sock.connect(("example.url.com", 80))
while True:
    # Receive a message
    recvMsg = sock.recv(1024)
    print("<SERVER SAYS>: " + recvMsg.decode())
    # Send a message
    sendMsg = "Hello World!"
    print("<SENDING MSG>: " + sendMsg.encode())
    sock.send(sendMsg.encode())
    # Timer to slow things down, if needed
    #sleep(5)

# Interactive mode

#t = Telnet()
#t.sock = sock
#t.interact()
#sock.close()
