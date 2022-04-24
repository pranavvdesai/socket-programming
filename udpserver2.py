import socket
import datetime
UDP_IP = "127.0.0.1"
UDP_PORT = 5004
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
while True:
    data, addr = sock.recvfrom(1024)
    data_decode = data.decode()
    data_split = data_decode.split("/")
    date_time  = datetime.datetime.now()
    date_time_year = date_time.year
    date_time_month = date_time.month
    date_time_day = date_time.day
    year = abs(date_time_year - int(data_split[2]))
    month = abs(date_time_month - int(data_split[1]))
    day = abs(date_time_day - int(data_split[0]))
    sock.sendto(f"you are {year} years old, {month} months old and {day} days old".encode(),addr)