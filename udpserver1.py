import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 5002
file = open("udpserver1.txt", "w")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
while True:
    data, addr = sock.recvfrom(1024)
    fileContent = data.decode()
    print("received", fileContent)
    file.write(fileContent)
    file.close()
    sock.sendto("file content received".encode(), addr)