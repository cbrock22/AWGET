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
    #print(ssInfo)
    ssIndex=random.randint(0,totalSS-1)
    #ssIndex = 0 #comment this out when you are ready to test with multiple IP's on the list
    nextSS=ssInfo.pop(ssIndex)
    # print(ssInfo)
    #print(ssIndex)
    #print(nextSS)

    

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
    print("message being sent: \n", message)
    
    while True:
  
        # message sent to server
        s.send(message.encode('ascii'))
        
        # messaga received from server
        temp = ''
        while True:
            data = s.recv(1024)
            
            if not data:
                break
            temp += str(data)[2:-1]
        
        #data = data.decode("ascii")
        # print the received message
        #concatdata = ''.join(data)
        print('Received from the server :', temp)
        #print(len(concatdata))

        #HERE IS WHERE YOU WILL SAVE THE DATA FROM THE WGET REQUEST
        
        
        #print(data)
        
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