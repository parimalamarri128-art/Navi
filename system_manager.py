import subprocess


def shutdown_pc():
    subprocess.Popen(["shutdown", "/s", "/t", "0"])


def restart_pc():
    subprocess.Popen(["shutdown", "/r", "/t", "0"])


def lock_pc():
    subprocess.Popen(["rundll32.exe", "user32.dll,LockWorkStation"])


def open_task_manager():
    subprocess.Popen(["taskmgr.exe"])


def open_control_panel():
    subprocess.Popen(["control.exe"])