# VMware_Player_check

import os
import subprocess
import time

Create task in task scheduler for this Final.py to run on login
Final.py is the final

The check for the vmplayer.exe process is done every 30 min
Once vmplayer.exe is taken down or during a reboot, vmware should be restart with desired vm if it is allready not running.

