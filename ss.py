###############################################
# Group Name  : Uber

# Member1 Name: Cole Brock
# Member1 SIS ID: 831823119
# Member1 Login ID: cbrock22

# Member2 Name: XXXXXX
# Member2 SIS ID: XXXXXX
# Member2 Login ID: XXXXXX

# Member3 Name: Zach Walsh
# Member3 SIS ID: 831955300
# Member3 Login ID: zachwals
###############################################
from __future__ import unicode_literals
import sys
import os
import random
import socket
from socket import AF_INET, SOCK_STREAM
from threading import Thread
from socketserver import ThreadingMixIn

class ClientThread(Thread):

    def __init__(self, ip, port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        print("[+] a new thread has started on {}:{}".format(ip,port))

    def run(self):
        while True:
            try:
                data = c.recv(262144)
                data = (data.decode("ascii"))
                # print(data)
                # print(data[len(data)-10:len(data)-1])

                x = data.split('\n')
                url = x.pop(0)
                y = url.split('/')
                filename = y.pop()
                # print(filename)
                if len(x) == 0:
                    # print("the list is empty!")
                    os.system("wget -O tFile {}".format(url))
                    f = open('./tFile', 'rb')
                    #awgetresponse = f.read()
                    
                    #print(len(awgetresponse))
                    
                    #awgetresponse  = str(awgetresponse)
                    
                    
                    #awgetresponse+=("response\n")
                    
                    #print(len(awgetresponse))
                    while True:
                        message = f.read(1024)
                        # print(message)
                        if not message:
                            break
                        c.send(message)    
                if len(x) != 0:
                    # print("the list is not empty!")
                    randindex = random.randint(0, len(x)-1)
                    nextss = x.pop(randindex)
                    nextss.split(' ')
                    soc2 = socket.socket(AF_INET, SOCK_STREAM)
                    soc2.connect(nextss[0], nextss[1])
                    print("ss has connected to nextss with IP: {} and port: {}".format(nextss[0], nextss[1]))
                    message = url
                    message += str(x)
                    soc2.send(message)
                    while True:
                        data2 = soc2.recv(1024)
                        if not data2:
                            break
                        c.send(data2)
                    soc2.close()
                    c.close()
                break
            except KeyboardInterrupt:
                break


if(len(sys.argv) != 2):
    print('Please specify only one port number.')
    exit(1)
portNum = sys.argv[1]
print('starting stepper...')
conn = socket.gethostname()
#print(conn)
IP = socket.gethostbyname(conn)
#print(IP)
soc = socket.socket(AF_INET, SOCK_STREAM)
soc.bind(('127.0.0.1', int(portNum)))
soc.listen(5)
#print('socket with IP {} on port {} is listening...'.format(IP,portNum))
threads = []

while True:
    try:
        (c, (sourceip,sourceport)) = soc.accept()
        newthread = ClientThread(sourceip,portNum)
        newthread.start()
        threads.append(newthread)
        break
    except KeyboardInterrupt:
        c.close()
        soc.close()
        break

for t in threads:
    t.join()

