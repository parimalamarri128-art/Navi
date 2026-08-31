import subprocess


# =========================================================
# BATTERY
# =========================================================

def battery_information():
    try:
        result = subprocess.run(
            [
                "powershell",
                "-NoProfile",
                "-Command",
                "Get-CimInstance Win32_Battery | "
                "Select-Object Name, BatteryStatus, EstimatedChargeRemaining, "
                "EstimatedRunTime | Format-List"
            ],
            capture_output=True,
            text=True
        )

        output = result.stdout.strip()

        if not output:
            return "No battery information found. This PC may not have a battery."

        return "Battery Information:\n" + output

    except Exception as e:
        return f"Could not get battery information: {e}"


# =========================================================
# BIOS
# =========================================================

def bios_information():
    try:
        result = subprocess.run(
            [
                "powershell",
                "-NoProfile",
                "-Command",
                "Get-CimInstance Win32_BIOS | "
                "Select-Object Manufacturer, SMBIOSBIOSVersion, "
                "ReleaseDate | Format-List"
            ],
            capture_output=True,
            text=True
        )

        output = result.stdout.strip()

        if not output:
            return "BIOS information not found."

        return "BIOS Information:\n" + output

    except Exception as e:
        return f"Could not get BIOS information: {e}"


# =========================================================
# GPU / DISPLAY
# =========================================================

def gpu_information():
    try:
        result = subprocess.run(
            [
                "powershell",
                "-NoProfile",
                "-Command",
                "Get-CimInstance Win32_VideoController | "
                "Select-Object Name, DriverVersion, "
                "VideoMemoryType, AdapterRAM | Format-List"
            ],
            capture_output=True,
            text=True
        )

        output = result.stdout.strip()

        if not output:
            return "GPU information not found."

        return "GPU / Display Information:\n" + output

    except Exception as e:
        return f"Could not get GPU information: {e}"


# =========================================================
# STORAGE DRIVES
# =========================================================

def storage_information():
    try:
        result = subprocess.run(
            [
                "powershell",
                "-NoProfile",
                "-Command",
                "Get-CimInstance Win32_LogicalDisk | "
                "Where-Object {$_.DriveType -eq 3} | "
                "Select-Object DeviceID, VolumeName, Size, FreeSpace | "
                "Format-Table -AutoSize"
            ],
            capture_output=True,
            text=True
        )

        output = result.stdout.strip()

        if not output:
            return "Storage information not found."

        return "Storage Drives:\n" + output

    except Exception as e:
        return f"Could not get storage information: {e}"


# =========================================================
# USB DEVICES
# =========================================================

def usb_devices():
    try:
        result = subprocess.run(
            [
                "powershell",
                "-NoProfile",
                "-Command",
                "Get-CimInstance Win32_USBControllerDevice | "
                "ForEach-Object {$_.Dependent} | "
                "ForEach-Object {Get-CimInstance -InputObject $_} | "
                "Select-Object Name, Manufacturer | "
                "Format-Table -AutoSize"
            ],
            capture_output=True,
            text=True
        )

        output = result.stdout.strip()

        if not output:
            return "No USB device information found."

        return "USB Devices:\n" + output

    except Exception as e:
        return f"Could not get USB information: {e}"


# =========================================================
# MOTHERBOARD
# =========================================================

def motherboard_information():
    try:
        result = subprocess.run(
            [
                "powershell",
                "-NoProfile",
                "-Command",
                "Get-CimInstance Win32_BaseBoard | "
                "Select-Object Manufacturer, Product, Version, SerialNumber | "
                "Format-List"
            ],
            capture_output=True,
            text=True
        )

        output = result.stdout.strip()

        if not output:
            return "Motherboard information not found."

        return "Motherboard Information:\n" + output

    except Exception as e:
        return f"Could not get motherboard information: {e}"