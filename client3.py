import socket
host = socket.gethostname()
port = 1452
s=socket.socket()
s.connect((host,port))

dataword = "1011"
count = 0
for i in dataword:
    if i == "1":
        count += 1

if count % 2 == 0:
    dataword = dataword + "0"
else:
    dataword = dataword + "1"

dataword_list = list(dataword)
dataword_list[1] = "1"
dataword = "".join(dataword_list)

s.send(dataword.encode())

print(s.recv(1024))
s.close()