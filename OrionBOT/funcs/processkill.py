import os
import platform         
def kill(proc_name):
    if platform.system() == "Windows":
        os.system(f'powershell -Command "Stop-Process -Name {proc_name} -Force"')
    if platform.system() == "Linux":
        os.system(f"pkill {proc_name}")