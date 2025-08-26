import platform
import os
import socket
import psutil
import getpass
import requests
import subprocess
import uuid
import random
from datetime import datetime
user=os.getlogin()
try:
    import GPUtil
except ImportError:
    GPUtil = None

# FIX: This can be a module, added in extern methods.

def get_hwid():
    system = platform.system()
    if system == "Windows":
        try:
            # Use Windows machine GUID
            import subprocess
            hwid = subprocess.check_output("wmic csproduct get uuid", shell=True).decode().split("\n")[1].strip()
            return hwid
        except Exception:
            return str(uuid.getnode())
    elif system == "Linux":
        try:
            with open("/etc/machine-id") as f:
                return f.read().strip()
        except Exception:
            try:
                return subprocess.check_output(["dmidecode", "-s", "system-uuid"]).decode().strip()
            except Exception:
                return str(uuid.getnode())
    return str(uuid.getnode())

def get_system_info():
    info = {}

    uname = platform.uname()
    info["HWID"] = get_hwid()
    info["System"] = uname.system
    info["Node Name"] = uname.node
    info["Release"] = uname.release
    info["Version"] = uname.version
    info["Machine"] = uname.machine
    info["Processor"] = uname.processor
    info["Boot Time"] = datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    info["User"] = getpass.getuser()

    # CPU info
    cpu_freq = psutil.cpu_freq()
    info["Physical Cores"] = psutil.cpu_count(logical=False)
    info["Total Cores"] = psutil.cpu_count(logical=True)
    if cpu_freq:
        info["Max Frequency (MHz)"] = cpu_freq.max
        info["Min Frequency (MHz)"] = cpu_freq.min
        info["Current Frequency (MHz)"] = cpu_freq.current
    info["CPU Usage per Core"] = psutil.cpu_percent(percpu=True, interval=1)
    info["Total CPU Usage"] = psutil.cpu_percent()

    # Memory info
    svmem = psutil.virtual_memory()
    info["Total RAM (GB)"] = round(svmem.total / (1024 ** 3), 2)
    info["Available RAM (GB)"] = round(svmem.available / (1024 ** 3), 2)
    info["Used RAM (GB)"] = round(svmem.used / (1024 ** 3), 2)
    info["RAM Usage (%)"] = svmem.percent

    swap = psutil.swap_memory()
    info["Total Swap (GB)"] = round(swap.total / (1024 ** 3), 2)
    info["Used Swap (GB)"] = round(swap.used / (1024 ** 3), 2)
    info["Free Swap (GB)"] = round(swap.free / (1024 ** 3), 2)

    # Disk info
    disk_info = []
    for partition in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            disk_info.append({
                "Device": partition.device,
                "Mountpoint": partition.mountpoint,
                "Fstype": partition.fstype,
                "Total (GB)": round(usage.total / (1024 ** 3), 2),
                "Used (GB)": round(usage.used / (1024 ** 3), 2),
                "Free (GB)": round(usage.free / (1024 ** 3), 2),
                "Usage (%)": usage.percent,
            })
        except PermissionError:
            continue
    info["Disks"] = disk_info

    # GPU info
    if GPUtil:
        try:
            gpus = GPUtil.getGPUs()
            gpu_info = []
            for gpu in gpus:
                gpu_info.append({
                    "Name": gpu.name,
                    "Memory Total (MB)": gpu.memoryTotal,
                    "Memory Used (MB)": gpu.memoryUsed,
                    "Memory Free (MB)": gpu.memoryFree,
                    "Driver": gpu.driver,
                    "GPU Load (%)": gpu.load * 100,
                    "Temperature (°C)": gpu.temperature,
                })
            info["GPUs"] = gpu_info
        except Exception:
            info["GPUs"] = "Error retrieving GPU info"

    return info

def get_network_info():
    net_info = {}

    # Interfaces
    addrs = psutil.net_if_addrs()
    stats = psutil.net_if_stats()
    interfaces = {}
    for iface, addr_list in addrs.items():
        iface_details = {
            "Is Up": stats[iface].isup if iface in stats else None,
            "Speed (Mbps)": stats[iface].speed if iface in stats else None,
            "MAC": None,
            "IPv4": None,
            "IPv6": None,
        }
        for addr in addr_list:
            if addr.family == socket.AF_INET:
                iface_details["IPv4"] = addr.address
            elif addr.family == socket.AF_INET6:
                iface_details["IPv6"] = addr.address
            elif addr.family == psutil.AF_LINK:
                iface_details["MAC"] = addr.address
        interfaces[iface] = iface_details
    net_info["Interfaces"] = interfaces

    # Public IP and ISP
    try:
        r = requests.get("https://ipinfo.io/json", timeout=5)
        if r.status_code == 200:
            data = r.json()
            net_info["Public IP"] = data.get("ip")
            net_info["ISP"] = data.get("org")
            net_info["City"] = data.get("city")
            net_info["Region"] = data.get("region")
            net_info["Country"] = data.get("country")
            net_info["Location"] = data.get("loc")
    except Exception as e:
        net_info["Public IP Error"] = str(e)

    # Active connections
    connections = []
    for conn in psutil.net_connections(kind="inet"):
        try:
            connections.append({
                "LAddr": f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else None,
                "RAddr": f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else None,
                "Status": conn.status,
                "PID": conn.pid
            })
        except Exception:
            continue
    net_info["Connections"] = connections

    return net_info

def save_file(content): # TODO: No disk, no trace. Please convert it to memory-file
    filename = "netstat.log"

    if platform.system() == "Linux":
        base = f"/home/{user}/.local/share/"
    elif platform.system() == "Windows":
        base = f"C:\\Users\\{user}\\AppData\\Local"
    else:
        base = "./"

    os.makedirs(base, exist_ok=True)
    path = os.path.join(base, filename)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    return path

def run():
    sysinfo = get_system_info()
    netinfo = get_network_info()
    lines = []
    lines.append("==== SYSTEM INFORMATION ====")
    for k, v in sysinfo.items():
        if isinstance(v, list):
            lines.append(f"{k}:")
            for item in v:
                lines.append(f"  {item}")
        elif isinstance(v, dict):
            lines.append(f"{k}:")
            for subk, subv in v.items():
                lines.append(f"  {subk}: {subv}")
        else:
            lines.append(f"{k}: {v}")
    lines.append("\n==== NETWORK INFORMATION ====")
    for k, v in netinfo.items():
        if isinstance(v, list):
            lines.append(f"{k}:")
            for item in v:
                lines.append(f"  {item}")
        elif isinstance(v, dict):
            lines.append(f"{k}:")
            for subk, subv in v.items():
                lines.append(f"  {subk}: {subv}")
        else:
            lines.append(f"{k}: {v}")
    content = "\n".join(lines)
    filepath = save_file(content)
    print(f"System info saved to {filepath}")
