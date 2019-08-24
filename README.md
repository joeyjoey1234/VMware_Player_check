# VMware_Player_check

import os
import subprocess
import time
In Final Script, Make sure to replace my .vmx file location with your .vmx file of the machine you wish to run
Create task in task scheduler for this Final.py to run on login
Final.py is the final for version 1.0
The check for the vmplayer.exe process is done every 30 min
Once vmplayer.exe is taken down or during a reboot, vmware should be restart with desired vm if it is allready not running.

Version 2.00
import os
import subprocess
import time
***import win32gui
Uses win32gui
finds a specfic VM window title and and runs that vm ,
Please tailor to your case, right now it runs my ssh server if it ever isnt running.


