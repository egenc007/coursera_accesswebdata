#recieving data from a website by requesting i

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connects to the 80 port
mysock.connect(('data.pr4e.org', 80))

#encode() converts from unicode internally to UTF-8
cmd = 'GET https//data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()

#send the command
mysock.send(cmd)

while True:
    #ask up to 512 chars of data
    data = mysock.recv(512)
    #if there is no data break the loop
    if (len(data) < 1):
        break

    #decode() converts UTF-8 to unicode
    print(data.decode())

#then end it
mysock.close()

