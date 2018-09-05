#!/usr/bin/python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("Target IP", 21))
res = s.res
print res

#! ./ftpenum.py
