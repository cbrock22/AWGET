###############################################
# Group Name  : Uber

# Member1 Name: Cole Brock
# Member1 SIS ID: 831823119
# Member1 Login ID: cbrock22

# Member2 Name: Alanood Alqobaisi
# Member2 SIS ID: 832901420
# Member2 Login ID: alanood

# Member3 Name: Zach Walsh
# Member3 SIS ID: 83195530
# Member3 Login ID: zachwals
###############################################
# Import socket module
import socket
import sys
import random

def Main(argv):

    # read file
    url=""
    filename="chaingang.txt"
    ssInfo=[]
    totalSS=0
    if len(argv)==1:
        url=argv[0]
    elif len(argv)==2:
        url=argv[0]
        filename=argv[1]
    else:
        print("error")
        return 1
    
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
        
    # print(url)
    # print(ssInfo)
    ssIndex=random.randint(0,totalSS-1)
    nextSS=ssInfo.pop(ssIndex)
    # print(ssInfo)
    # print(ssIndex)
    # print(nextSS)

    

    # local host IP '127.0.0.1'
    host = nextSS[0] 
    # host = '127.0.0.1' #Local Host overwrite
  
    # Define the port on which you want to connect
    port = nextSS[1]
    # port = 2000 #Local Host Overwrite
  
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    # connect to server on local computer
    s.connect((host,port))
  
    # message you send to server
    message=url
    for x in ssInfo:

        message=message+"\n"+str(x[0])+" "+str(x[1])
    print(message)
    
    while True:
  
        # message sent to server
        s.send(message.encode('ascii'))
  
        # messaga received from server
        data = s.recv(1024)
  
        # print the received message
        # here it would be a reverse of sent message
        print('Received from the server :',str(data.decode('ascii')))
  
        # ask the client whether he wants to continue
        ans = input('\nDo you want to continue(y/n) :')
        if ans == 'y':
            continue
        else:
            break
    # close the connection
    s.close()
  
if __name__ == '__main__':
    Main(sys.argv[1:])