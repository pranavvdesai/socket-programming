import socket
s = socket.socket()
host = socket.gethostname()
port = 1600
s.connect((host, port))
s.send("1x^2-5x-14=0".encode())
print(s.recv(1024))
s.close()