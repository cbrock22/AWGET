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

import sys
import socket
from socket import AF_INET, SOCK_STREAM

# def threaded(c):
#     while c:
#         data = c.recv(1024)
#         if not data:
#             print('No message close connection')
#             print_lock.release()

def stepper(portNum):
    print('starting stepper...')
    conn = socket.gethostname()
    print(conn)
    IP = socket.gethostbyname(conn)
    print(IP)
    soc = socket.socket(AF_INET, SOCK_STREAM)
    soc.bind(('127.0.0.1', int(portNum)))
    soc.listen(5)
    print('socket with IP {} on port {} is listening...'.format(IP,portNum))
    threads = []

    #while True:
    c, addr = soc.accept()
    data = c.recv(1024)
    print('data recieved from {} :'.format(addr))
    print('')
    print(data)
    print('')
    print('exiting program')
    c.close()
    soc.close()




def main():
    if(len(sys.argv) != 2):
        print('Please specify only one port number.')
        exit(1)
    stepper(sys.argv[1])


if __name__ == "__main__":
    main()