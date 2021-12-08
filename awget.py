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
import socket
import sys
import random
import os
from urllib.parse import urlparse

def Main(argv):
    url=""
    filename="chaingang.txt"
    ssInfo=[]
    totalSS=0
    print("awget:")
    if len(argv)==1:
        url=argv[0]
        
    elif len(argv)==3 and argv[1]=="-c":
        url=argv[0]
        filename=argv[2]
    else:
        print("Bad Args")
        return 1
    print(f"Request: {url}")
    try:    
        f=open(filename)
        data=f.readlines()
        
        f.close()
        totalSS=int(data[0][0])
        for x in range(int(totalSS)):
            if(x+1<=totalSS):
                tIp,tPort=data[x+1].split()
                ssInfo.append((tIp,int(tPort)))
    
    except:
        print("error")
        return 1
    print("chainlist is:")
    for s in ssInfo:
        print(s)
    ssIndex=random.randint(0,totalSS-1)
    nextSS=ssInfo.pop(ssIndex)
    host = nextSS[0] 
    # host = '127.0.0.1' #Local Host overwrite
    port = nextSS[1]
    print(f"Next ss is {nextSS}")
    # port = 2000 #Local Host Overwrite
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((host,port))
    message=url
    for x in ssInfo:

        message=message+"\n"+str(x[0])+" "+str(x[1])
    
    s.send(message.encode('ascii'))
    temp = ''
    print("Waiting for file...")
    while True:
        data = s.recv(1024)
        if not data:
            break
        temp += data.decode("ISO-8859-1")
    filen=get_filename(url)
    f2=open(filen,'w')
    f2.write(temp)
    print(f"Url:{url} found. File saved as {filen}")
    f2.close()
    # close the connection
    s.close()
    print("Goodbye!")

def get_filename(url):
    a = urlparse(url)
    filename = os.path.basename(a.path)
    if len(filename)<=0 or '/' not in url:
        filename = "index.html"
    return filename

  
if __name__ == '__main__':
    Main(sys.argv[1:])