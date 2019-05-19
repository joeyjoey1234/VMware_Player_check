import subprocess
import os

def vm_player_check():
    data = os.popen('tasklist /FI "IMAGENAME eq vmplayer.exe"').read()
    data = str(data)
    data = data.split()
    if 'vmplayer.exe' in data:
        print(True)
    else:
        print(False)

vm_player_check()