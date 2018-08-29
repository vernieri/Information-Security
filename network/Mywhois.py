#!/usr/share/python
import socket, sys

ip = raw_input("Target IP: ")
port = input("Target Port: ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(ip, port)
s.send("Web site\r\n")
resp = s.recv(1024)
print resp

