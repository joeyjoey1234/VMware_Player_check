import subprocess
import os
import time
import win32gui

win2find = 'SSH server - VMware Workstation 15 Player'
whnd = win32gui.FindWindowEx(None, None, None, win2find)

def vm_player_check():
    if whnd == 0:
        return False  
    else:
        return True


def run_ssh_server(c):
    if c == False:
        print("starting vm ssh server")
        #### This line call upon vmplayer.exe and your .vmx file for the vm you want to run
        subprocess.call(['C:\Program Files (x86)\VMware\VMware Player\\vmplayer.exe','E:\ssh server\SSH server.vmx'])
    else:
        print('ssh server is running')
        pass

### run in python console to see the debug info
while True:
    run_ssh_server(vm_player_check())
    print("starting sleep")
    time.sleep(1800)
    print('ending sleep loop')


