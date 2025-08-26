import os

def exec(cmd: str) -> int:
    return os.system(cmd)

def reboot():
    if os.name == "nt":
        os.system('shutdown /r /t 0 /f')
    else:
        os.system('reboot now')

def shutdown():
    if os.name == "nt":
        os.system('shutdown /s /t 0 /f')
    else:
        os.system('shutdown now')
