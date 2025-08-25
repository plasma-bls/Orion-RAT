import platform
import os
import psutil

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
        base = "/home/plasma/.local/share/"
    elif platform.system() == "Windows":
        base = os.environ['APPDATA'].replace("Roaming", "LocalLow") + "\\"
    else:
        base = "./"
    return os.path.join(base, "processes_info.txt")

if __name__ == "__main__":
    file_path = get_file_path()
    procs = get_processes()
    lines = [str(proc) for proc in procs]
    save_file(file_path, lines)
    print(f"Processes info saved to {file_path}")
