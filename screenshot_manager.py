import os
from datetime import datetime
import pyautogui

def take_screenshot():
    username = os.environ.get("USERNAME")

    folder = os.path.join(
        "C:\\Users",
        username,
        "Pictures",
        "Screenshots"
    )

    os.makedirs(folder, exist_ok=True)

    filename = datetime.now().strftime(
        "Screenshot_%Y%m%d_%H%M%S.png"
    )

    path = os.path.join(folder, filename)

    pyautogui.screenshot(path)

    return f"Screenshot saved:\n{path}"