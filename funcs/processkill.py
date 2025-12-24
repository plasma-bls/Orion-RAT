import os
import platform         
def kill(proc_name):
    if platform.system() == "Windows":
        os.system(f'taskkill /IM {proc_name}.exe /F')
    if platform.system() == "Linux":
        os.system(f"pkill {proc_name}")
