import subprocess
import os
import time

def vm_player_check():
    data = os.popen('tasklist /FI "IMAGENAME eq vmplayer.exe"').read()
    data = str(data)
    data = data.split()
    if 'vmplayer.exe' in data:
        return True
    else:
        return False


def run_ssh_server(c):
    if c == False:
        print("starting vm ssh server")
        #### This line call upon vmplayer.exe and your .vmx file for the vm you want to run
        subprocess.call(['C:\Program Files (x86)\VMware\VMware Player\\vmplayer.exe','E:\ssh server\SSH server.vmx'])
    else:
        print('ssh server is running')
        pass


while True:
    run_ssh_server(vm_player_check())
    print("starting sleep")
    time.sleep(1800)
    print('ending sleep loop')


