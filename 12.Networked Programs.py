#Sockets are like making a phone call, applications ontop of it is like what you say in that phone call

import socket
import urllib
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
'''
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))

message = 'GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n'
message.encode()

mysock.send(message.encode())

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ):
        break
    print(data)
mysock.close()
'''

#Using urllib
#-turns url to act like files

fhand = urllib.request.urlopen(('http://www.py4inf.com/code/romeo.txt'))
for line in fhand:
    print(line.strip())

