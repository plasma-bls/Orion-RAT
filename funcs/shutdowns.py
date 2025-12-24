import platform
import os
def run():
    if platform.system() == "Linux":
        os.system('shutdown now')
    if platform.system() == "Windows":
        os.system('shutdown /s /t 0 /f')