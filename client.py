import socket
s = socket.socket()
host = socket.gethostname()
port = 1600
s.connect((host, port))
s.send(b'Hello server!')
print(s.recv(1024))
s.close()