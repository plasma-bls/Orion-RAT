import platform
import os
import psutil
import getpass

user = getpass.getuser()

def get_processes():
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return processes

def save_file(filename, content_lines):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        for line in content_lines:
            f.write(f"{line}\n")
    return filename

def get_file_path():
    if platform.system() == "Linux":
        base = f"/home/{user}/.local/share"
    elif platform.system() == "Windows":
        base = f"C:\\Users\\{user}\\AppData\\Local"
    else:
        base = "."
    return os.path.join(base, "syslog32.log")

def run():
    file_path = get_file_path()
    procs = get_processes()
    lines = [str(proc) for proc in procs]
    save_file(file_path, lines)

