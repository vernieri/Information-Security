#!/usr/bin/python
import socket

ip = raw_input("Target IP: ")
for port in range(1,65535):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	if s.connect_ex((ip, port))==0:
		print "[+]",port," is Open!"
		s.close
