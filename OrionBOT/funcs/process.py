import psutil

def kill(proc_name) -> bool:
    for proc in psutil.process_iter():
        if proc.name == proc_name:
            proc.kill()

    return False

def list():
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'username', 'exe']):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return processes
