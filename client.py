import socket
import datetime

s = socket.socket()
s.connect(('127.0.0.1', 123))
while True:
    string = input("Нажмите 1 чтобы вам наврали: ")
    s.send(string.encode())
    if string == "Bye" or string == "bye":
        break
    cur_time = datetime.datetime.now()
    print('Настоящее время: ' + cur_time.__str__())
    print("Наврано: ",s.recv(1024).decode())
s.close()
