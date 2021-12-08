###############################################
# Group Name  : Uber

# Member1 Name: Cole Brock
# Member1 SIS ID: 831823119
# Member1 Login ID: cbrock22

# Member2 Name: Alanood Alqobaisi
# Member2 SIS ID: 832901420
# Member2 Login ID: alanood

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
                data = c.recv(264144)
                data = (data.decode("ascii"))
                x = data.split('\n')
                url = x.pop(0)

                if len(x) == 0:
                    os.system("wget -O tFile {}".format(url))
                    f = open('tFile', 'rb')
                    while True:
                        message = f.read(1024)
                        if not message:
                            break
                        c.send(message)
                    f.close()
                    os.system("rm ./tFile")
                    break
                if len(x) != 0:
                    ssInfo=[]
                    for t in range(int(len(x))):
                        if(t<=len(x)):
                            tIp,tPort=x[t].split()
                            ssInfo.append((tIp,int(tPort)))
                    ssIndex=random.randint(0,len(x)-1)
                    nextip,nextp=ssInfo.pop(ssIndex)
                    soc2 = socket.socket(AF_INET, SOCK_STREAM)
                    soc2.connect((nextip, nextp))
                    message = url
                    for t in ssInfo:
                        message=message+'\n'+str(t[0]+" "+str(t[1]))
                    soc2.send(message.encode("ascii"))
                    while True:
                        data2 = soc2.recv(1024)
                        if not data2:
                            break
                        c.send(data2)
                    soc2.close()
                    break
                
            except KeyboardInterrupt:
                soc2.close()
                c.close()
                exit(1)
        c.close()
        print("[-] thread with IP : {} and port {} connection closed, going back to listening...".format(self.ip, self.port))
        return


if(len(sys.argv) != 3):
    print('incorrect arguments')
    print('correct usage : python3 ss.py -p [port number]')
    exit(1)
portNum = sys.argv[2]

conn = socket.gethostname()
IP = socket.gethostbyname(conn)
soc = socket.socket(AF_INET, SOCK_STREAM)
soc.bind((IP, int(portNum)))
soc.listen(5)
print('Starting Stepping Stone with IP : {} on port : {} ... '.format(IP,portNum))
threads = []

while True:
    try:
        
        (c, (sourceip,sourceport)) = soc.accept()
        newthread = ClientThread(sourceip,portNum)
        newthread.start()
        threads.append(newthread)
    except KeyboardInterrupt:
        soc.close()
        break

for t in threads:
    t.join()