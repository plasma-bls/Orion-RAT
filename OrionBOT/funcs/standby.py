import os
import platform
def run():
    if platform.system() == "Linux":
        os.system('systemctl suspend')
    if platform.system() == "Windows":
        os.system('rundll32.exe powrprof.dll,SetSuspendState Sleep')