import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 5004
birthdate = input("enter bday")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(birthdate.encode(), (UDP_IP, UDP_PORT))
print(sock.recv(1024).decode())