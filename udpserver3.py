import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 5007
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    data_decode = data.decode()
    t=-1
    sub_part = data_decode.split(".")
    total_address = 2**8
    sock.sendto(("total number of addresses: " + str(total_address)).encode(),addr)
    subnets_add = int(total_address/8)
    sock.sendto(("number of subnets address in each subnet: " + str(subnets_add)).encode(),addr)

    for i in range(8):
        t+=1
        start = t
        t+=(subnets_add-1)
        end = t
        sock.sendto(("start address of subnet" + str(i+1) + ": " + sub_part[0] + "." + sub_part[1] + "." + sub_part[2] + "." + str(start) ).encode(),addr)
        sock.sendto(("end address of subnet" + str(i+1) + ": " + sub_part[0] + "." + sub_part[1] + "." + sub_part[2] + "." + str(end) ).encode(),addr)
