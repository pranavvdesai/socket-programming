import socket
import datetime
s = socket.socket()
host = socket.gethostname()
port = 1600
s.bind((host, port))
s.listen(5)
print("Server is listening on port:", port)
while True:
    c, addr = s.accept()
    print("Got connection from", addr)
    c.send(str(datetime.datetime.now()).encode())
    print(c.recv(1024))
    c.close()