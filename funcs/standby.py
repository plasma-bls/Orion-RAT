import subprocess
import platform
import ctypes

def windows_suspend():
    """
    Attempt to suspend Windows.
    Checks if S3 sleep is available before calling the API.
    Falls back gracefully if not supported.
    """
    try:
        # Check available sleep states
        result = subprocess.run("powercfg /a", capture_output=True, text=True, shell=True)
        output = result.stdout.lower()

        if "standby (s3)" in output:
            ctypes.windll.PowrProf.SetSuspendState(False, True, False)
        elif "standby (s0 low power idle)" in output:
            return "Modern Standby (S0ix) detected. Cannot force suspend from script."
        else:
            return "No suspend state available on this machine."
    except Exception as e:
        return f"Failed to suspend Windows: {e}"

def linux_suspend():

    try:
        subprocess.call("systemctl suspend", shell=True)
    except Exception as e:
        return f"Failed to suspend Linux: {e}"
def suspend_system():
    system = platform.system()
    if system == "Windows":
        windows_suspend()
    elif system == "Linux":
        linux_suspend()
    else:
        return f"Suspend not implemented for {system}"
if __name__ == "__main__":
    suspend_system()
