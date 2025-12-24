import platform
import os
def run():
    if platform.system() == "Linux":
        os.system('reboot now')
    if platform.system() == "Windows":
        os.system('shutdown /r /t 0 /f')