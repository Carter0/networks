import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("cbw.sh", 27993))
s.send("cs3700spring2019 HELLO 001702072\n")