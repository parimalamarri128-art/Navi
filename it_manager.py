import os
import platform
import shutil
import socket
import subprocess

try:
    import psutil
except ImportError:
    psutil = None


# =========================================================
# CPU
# =========================================================

def check_cpu():
    if psutil is None:
        return "CPU information requires psutil."

    try:
        usage = psutil.cpu_percent(interval=1)
        cores = psutil.cpu_count(logical=False)
        threads = psutil.cpu_count(logical=True)

        return (
            f"CPU Usage: {usage}%\n"
            f"Physical Cores: {cores}\n"
            f"Logical Processors: {threads}"
        )

    except Exception as e:
        return f"Could not get CPU information: {e}"


# =========================================================
# RAM
# =========================================================

def check_ram():
    if psutil is None:
        return "RAM information requires psutil."

    try:
        memory = psutil.virtual_memory()

        total = memory.total / (1024 ** 3)
        used = memory.used / (1024 ** 3)
        available = memory.available / (1024 ** 3)

        return (
            f"RAM Total: {total:.2f} GB\n"
            f"RAM Used: {used:.2f} GB\n"
            f"RAM Available: {available:.2f} GB\n"
            f"RAM Usage: {memory.percent}%"
        )

    except Exception as e:
        return f"Could not get RAM information: {e}"


# =========================================================
# DISK
# =========================================================

def check_disk():
    try:
        disk = shutil.disk_usage("C:\\")

        total = disk.total / (1024 ** 3)
        used = disk.used / (1024 ** 3)
        free = disk.free / (1024 ** 3)

        percent = (disk.used / disk.total) * 100

        return (
            f"Disk: C:\\\n"
            f"Total: {total:.2f} GB\n"
            f"Used: {used:.2f} GB\n"
            f"Free: {free:.2f} GB\n"
            f"Usage: {percent:.1f}%"
        )

    except Exception as e:
        return f"Could not get disk information: {e}"


# =========================================================
# SYSTEM INFORMATION
# =========================================================

def system_information():
    try:
        return (
            f"Computer: {platform.node()}\n"
            f"System: {platform.system()}\n"
            f"Release: {platform.release()}\n"
            f"Version: {platform.version()}\n"
            f"Machine: {platform.machine()}\n"
            f"Processor: {platform.processor()}"
        )

    except Exception as e:
        return f"Could not get system information: {e}"


# =========================================================
# WINDOWS VERSION
# =========================================================

def windows_version():
    try:
        result = subprocess.run(
            "winver",
            shell=True
        )

        return "Windows version information opened."

    except Exception as e:
        return f"Could not open Windows version information: {e}"


# =========================================================
# IP ADDRESS
# =========================================================

def show_ip():
    try:
        hostname = socket.gethostname()

        ip_address = socket.gethostbyname(hostname)

        return (
            f"Computer Name: {hostname}\n"
            f"IP Address: {ip_address}"
        )

    except Exception as e:
        return f"Could not get IP address: {e}"


# =========================================================
# DEVICE MANAGER
# =========================================================

def open_device_manager():
    try:
        subprocess.Popen("devmgmt.msc", shell=True)
        return "Device Manager opened."

    except Exception as e:
        return f"Could not open Device Manager: {e}"


# =========================================================
# TASK MANAGER
# =========================================================

def open_task_manager():
    try:
        subprocess.Popen("taskmgr.exe", shell=True)
        return "Task Manager opened."

    except Exception as e:
        return f"Could not open Task Manager: {e}"


# =========================================================
# SERVICES
# =========================================================

def open_services():
    try:
        subprocess.Popen("services.msc", shell=True)
        return "Services opened."

    except Exception as e:
        return f"Could not open Services: {e}"


# =========================================================
# EVENT VIEWER
# =========================================================

def open_event_viewer():
    try:
        subprocess.Popen("eventvwr.msc", shell=True)
        return "Event Viewer opened."

    except Exception as e:
        return f"Could not open Event Viewer: {e}"