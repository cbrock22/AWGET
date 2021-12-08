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
                # print(data)
                # print(data[len(data)-10:len(data)-1])
                x = data.split('\n')
                print("this is x at the start")
                print(x)
                url = x.pop(0)
                if(len(x) == 1 and x[0] == '[]'):
                    x.pop()
                print("this is the url in the beginning {}".format(url))
                print(url)
                y = url.split('/')
                filename = y.pop()
                #print(filename)
                if len(x) == 0:

                    os.system("wget -O tFile {}".format(url))
                    
                    f = open('tFile', 'rb')

                    while True:
                        message = f.read(1024)
                        #message = str(message)
                        # print(message)
                        #c.send("-1-".encode("ascii"))
                        if not message:
                            break
                        c.send(message)
                    break
                if len(x) != 0:
                    # print("the list is not empty!")
                    randindex = random.randint(0, len(x)-1)
                    nextss = x.pop(randindex)
                    print(nextss)
                    nextp = ''
                    nextip = ''
                    flag = False
                    for char in nextss:
                        if(char == ' '):
                            flag = True
                        if(flag == False):
                            nextip += char
                        elif(flag):
                            nextp += char
                    nextp = int(nextp)
                    print("hopeful ip ",nextip)
                    print("hopeful port ",nextp)
                    soc2 = socket.socket(AF_INET, SOCK_STREAM)
                    soc2.connect((nextip, nextp))
                    print("Connected to Next Stepping Stone {}:{}".format(nextip, nextp))
                    url = url + '\n'
                    message = url
                    
                    message += str(x)
                    soc2.send(message.encode("ascii"))
                    while True:
                        data2 = soc2.recv(1024)
                        if not data2:
                            break
                        c.send(data2)
                    soc2.close()
                
            except KeyboardInterrupt:
                soc2.close()
                c.close()
                exit(1)
        c.close()
        print("[-] thread with IP : {} and port {} connection closed, going back to listening...".format(self.ip, self.port))
        if(os.path.exists("tFile.txt")):
            os.system("rm tFile.txt")
        if(os.path.exists("tfilelog.txt")):
            os.system("rm tfilelog.txt")
        return


if(len(sys.argv) != 3):
    print('incorrect arguments')
    print('correct usage : python3 ss.py -p [port number]')
    exit(1)
portNum = sys.argv[2]

conn = socket.gethostname()
#print(conn)
IP = socket.gethostbyname(conn)
#print(IP)
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
        break #wont want this in final code - needs to go back to listening
    except KeyboardInterrupt:
        soc.close()
        exit(1)

for t in threads:
    t.join()

