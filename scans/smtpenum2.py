#!/usr/bin/python
import socket
import sys
import re

file = open('YOUR_LIST_HERE.txt')
for linha in file.readlines():
  s = socket.socket(socket.AF_INET, SOCK_STREAM)
  s.connect((sys.argv[1], 25))
  resp = s.recv(1024)
  s.send("VRFY"+linha)
  resp = s.recv(1024)
  if re.search('252', resp):
    print "[+] Usuario encontrado: "+resp
