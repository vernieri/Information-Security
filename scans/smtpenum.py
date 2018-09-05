#!/usr/bin/python
import socket
import sys

if len(sys.argv) != 3:
  print "Use: Python smtpenum.pi <Target IP> <User Name>
  sys.exit(0)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[1], 25))
banner = s.recv(1024)
print banner

s.send("VRFY"+sys.argv[2]+"\r\n")
r = s.recv(1024)
print r
