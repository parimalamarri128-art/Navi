import os
import subprocess
import shutil


def open_terminal():
    try:
        subprocess.Popen("wt.exe")
        return "Windows Terminal opened."
    except Exception:
        subprocess.Popen("cmd.exe")
        return "Command Prompt opened."


def open_cmd():
    subprocess.Popen("cmd.exe")
    return "Command Prompt opened."


def open_powershell():
    subprocess.Popen("powershell.exe")
    return "PowerShell opened."


def check_version(command, name):
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            shell=True
        )

        output = result.stdout.strip()

        if not output:
            output = result.stderr.strip()

        if output:
            return f"{name}:\n{output}"

        return f"{name} is not installed."

    except Exception:
        return f"Could not check {name}."


def check_python():
    return check_version("python --version", "Python")


def check_git():
    return check_version("git --version", "Git")


def check_node():
    return check_version("node --version", "Node.js")


def check_java():
    return check_version("java --version", "Java")


def open_program(program_paths, program_name):
    for path in program_paths:

        if os.path.exists(path):
            try:
                subprocess.Popen(path)
                return f"{program_name} opened."
            except Exception:
                pass

    found = shutil.which(program_name.lower())

    if found:
        try:
            subprocess.Popen(found)
            return f"{program_name} opened."
        except Exception:
            pass

    return f"{program_name} is not installed or could not be found."


def open_vscode():
    return open_program(
        [
           os.path.expandvars(
               r"%LOCALAPPDATA%\Programs\Microsoft VS Code\Code.exe"
 ),
            r"C:\Program Files\Microsoft VS Code\Code.exe",
            r"C:\Program Files (x86)\Microsoft VS Code\Code.exe",
        ],
        "code"
    )


def open_pycharm():
    return open_program(
        [
            r"C:\Program Files\JetBrains\PyCharm\bin\pycharm64.exe",
            r"C:\Program Files\JetBrains\PyCharm Community Edition\bin\pycharm64.exe",
        ],
        "pycharm"
    )


def open_visual_studio():
    return open_program(
        [
            r"C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\devenv.exe",
            r"C:\Program Files\Microsoft Visual Studio\2022\Professional\Common7\IDE\devenv.exe",
            r"C:\Program Files\Microsoft Visual Studio\2022\Enterprise\Common7\IDE\devenv.exe",
        ],
        "devenv"
    )


def open_android_studio():
    return open_program(
        [
            r"C:\Program Files\Android\Android Studio\bin\studio64.exe",
        ],
        "studio64"
    )


def open_intellij():
    return open_program(
        [
            r"C:\Program Files\JetBrains\IntelliJ IDEA\bin\idea64.exe",
        ],
        "idea64"
    )


def open_eclipse():
    return open_program(
        [
            r"C:\eclipse\eclipse.exe",
            r"C:\Program Files\Eclipse\eclipse.exe",
        ],
        "eclipse"
    )