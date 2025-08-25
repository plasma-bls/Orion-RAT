import os
import ctypes
import sys
import subprocess

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    print("This operation requires administrator privileges.")
    sys.exit(1)

target_path = r"C:\Windows\System32\config\OSDATA"

try:
    os.makedirs(target_path, exist_ok=True)
    print(f"Folder created at: {target_path}")
    
    # Force restart the PC
    print("The system will restart in 10 seconds. Save any open work.")
    subprocess.run(["shutdown", "/r", "/f", "/t", "10"])
    
except PermissionError:
    print("Permission denied. Even with admin rights, this is restricted.")
except Exception as e:
    print(f"Error: {e}")
