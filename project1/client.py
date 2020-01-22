import socket
import argparse


def CountOccurences(hostname, neuid, portNumber = 27993):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, portNumber))
    s.send(f'cs3700spring2020 HELLO {neuid}\n'.encode())


    while True:
        msg = ''

        while not msg.endswith('\n'):
            msg += s.recv(8192).decode()
            if msg == b'':
                raise RuntimeError("socket connection broken")

        splitString = msg.split()  
        if splitString[1] == "FIND": 
            toFind = splitString[2]
            foundCount = splitString[3].count(toFind)
            sent = s.send(f'cs3700spring2020 COUNT {foundCount}\n'.encode())
            if sent == 0:
                raise RuntimeError("socket connection broken")
        
        if splitString[1] == "BYE":
            print(msg)
            break

def main():
    parse = argparse.ArgumentParser(description='Count the occurences of every a char from server messages.')
    parse.add_argument("hostname", help="The hostname to connect to.", type=str)
    parse.add_argument("neuid", help="The NEU id to use.", type=str)
    parse.add_argument("-p", "--port", help="The port number to use.", type=int)
    args = parse.parse_args()

    if (args.port != None):
        print("here")
        CountOccurences(args.hostname, args.neuid, args.port)
    else:
        CountOccurences(args.hostname, args.neuid)

if __name__=='__main__':
    main()



            
        



        # Try recieving some thing here 
    

     
    



    