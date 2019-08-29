import subprocess
import os
import time
import win32gui

VM_ware_exe = 'C:\Program Files (x86)\VMware\VMware Player\\vmplayer.exe'

title1 = 'SSH server - VMware Workstation 15 Player'
title1_vmx = 'E:\ssh server\SSH server.vmx'

title2 = 'Web Server - VMware Workstation 15 Player'
title2_vmx = 'E:\Web Server\\Web Server.vmx'

title3 = 'virl.1.6.65.pc - VMware Workstation 15 Player'
title3_vmx = 'E:\Virl\\virl.1.6.65.pc.vmx'


titles = [title1, title2, title3]

def vm_player_check(x):
    whnd = win32gui.FindWindowEx(None, None, None, x)
    #print('Checking for {}'.format(x))
    if whnd == 0:
        if x == title1:
            # print("starting title1")
            subprocess.call([VM_ware_exe, title1_vmx])
        elif x == title2:
            # print("starting title2")
            subprocess.call([VM_ware_exe, title2_vmx])
            pass
        elif x == title3:
            # print("starting title3")
            subprocess.call([VM_ware_exe, title3_vmx])
            pass
        else:
            # print(Name error)
            pass
    else:
        print('program is running')
        pass




### run in python console and remove ## to see the debug info
while True:
    for x in titles:
        vm_player_check(x)
        print("starting sleep")
    time.sleep(1800)
    print('ending sleep loop')
