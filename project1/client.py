import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("fring.ccs.neu.edu", 27993))
s.send("cs3700spring2020 HELLO 001702072\n".encode())


while True:
    msg = ""

    #Read in everything up to the newline 
    while not msg.endswith('\n'):
        msg += s.recv(8192).decode()
        
    splitString = msg.split()
    if splitString[1] == "FIND": 
        print(msg)
        toFind = splitString[2]
        foundCount = splitString[3].count(toFind)
        s.send(f'cs3700spring2020 COUNT {foundCount}'.encode()) 

    if splitString[1] == "BYE":
        print("done")
        break 

    