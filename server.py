import socket 
import sys
from _thread import *

host = '127.0.0.1'
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host, port))
except socket.error as error:
    print(str(error))

s.listen(5)

print ('Listening....')

def thread_client(conn):
    conn.send(str.encode('HTTP/1.1 200 OK\r\nDate: Sun, 18 Oct 2012 10: 36: 20 GMT\r\nServer: Apache/2.2.14 (Win32)\r\nContent-Length: 230\r\nConnection: Closed\r\nContent-Type: text/html\r\ncharset=utf-8'))

    while True:
        data = conn.recv(2048)
        print(data)
        reply = 'Server output: ' + data.decode('utf-8')
        if not data:
            break
        conn.sendall(str.encode(reply))
    conn.close()


while True:
    conn, addr = s.accept()
    print('connected to ' + addr[0] + ':' + str(addr[1]))

    start_new_thread(thread_client,(conn,))
