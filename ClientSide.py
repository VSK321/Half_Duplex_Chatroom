import socket

LocalIPAddress = "127.0.0.1" #Enter your local ip address here
port = 444 #Enter a port number to bind the socket to. This can be an integer from 1 to 65535
data = ""
request = ""
ServerIPAddress = "127.0.0.1" #Enter the local ip address of the server
ServerPort = 44 #Enter the port on the server side

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
sock.bind((LocalIPAddress, port))

sock.connect((ServerIPAddress, ServerPort))
data = sock.recv(1024)
print(data.decode())
while data != "Exit":
    request = input("Type: ")
    sock.send(request.encode())
    data = sock.recv(4096)
    print(data.decode())

sock.close()
