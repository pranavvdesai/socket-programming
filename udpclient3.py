import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 5007
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = "212.56.70.0"
sock.sendto(data.encode(), (UDP_IP, UDP_PORT))
print(sock.recv(1024).decode())
print(sock.recv(1024).decode())
for i in range(8):
    print(sock.recv(1024).decode())
    print(sock.recv(1024).decode())