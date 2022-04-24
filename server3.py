from socket import socket


import socket
s=socket.socket()
host = socket.gethostname()
port = 1452

s.bind((host,port))
s.listen(5)
print("Server is listening on port:", port)
while True:
    c, a = s.accept()
    temp = 0
    syndrome = 0
    print("Got connection from", a)
    str_recv = c.recv(1024).decode()
    for i in str_recv:
        if i == "1":
            temp += 1

    if temp % 2 == 0:
        print(b"syndrome " + str(syndrome).encode())
        c.send(b"accepted" + str(syndrome).encode())
    else:
        syndrome = 1
        print(b"syndrome " + str(syndrome).encode())
        c.send(b"rejected" + str(syndrome).encode())
    c.close()