#!/usr/bin/python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("Target IP", 21))
res = s.recv(1024)
print res

s.send("USER anonymous \r\n")
x = s.recv(1024)
print x

s.send("PASS ANONYMOUS \r\n)
x = s.recv(1024)
print x

s.send("PWD \r\n")
s.send("QUIT \r\n")
x = s.recv(2048)
print x    
       
#! ./ftpenum.py
