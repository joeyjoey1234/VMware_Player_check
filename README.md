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


Version 3.00 ***********UPDATE***

More user friendly checks up to 3 titles
Change VM_ware_exe to the location of your vmware exe, You could honestly set this to any exe you want to run

Change Titles1-3 to the Window titles you wish to check for

Change titles1-3_vmx = to the vmx file you wish vmware to run, or use this as the opt for what ever you set as the VM_ware_exe

Change sleep_time to how long you want the rest times to be in seconds
