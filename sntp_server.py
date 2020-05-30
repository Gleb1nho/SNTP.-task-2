import socket
import datetime

s = socket.socket()
port = 123
s.bind(('localhost', port))
s.listen(5)
c, addr = s.accept()
while True:
    rcvdData = c.recv(4096).decode()
    print("S:",rcvdData)
    if(rcvdData == "Bye" or rcvdData == "bye"):
        break
    current_time = datetime.datetime.now()
    correction = int(open('config.txt').read().strip())
    sendData = (current_time + datetime.timedelta(seconds=correction)).__str__()
    c.send(sendData.encode())
    print('Наврал ^_^')
c.close()
