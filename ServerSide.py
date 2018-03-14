import socket

LocalIPAddress = socket.gethostbyname(socket.gethostname())
port = 0 #Enter a port number to bind the socket to. This can be an integer from 1 to 65535
data = ""
request = ""

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
sock.bind((LocalIPAddress, port))



sock.listen(1)
connection, addr = sock.accept()

print("You are connected to:", addr)
connection.send(("You are connected to the server").encode())
while request != "Exit":
    data = connection.recv(4096)
    print(data.decode())
    request = input("Type: ")
    connection.send(request.encode())

connection.close()
sock.close()
