import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 5002
file = open("udpclient1.txt", "r")
content = file.read()
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(content.encode(), (UDP_IP, UDP_PORT))
print(sock.recv(1024).decode())