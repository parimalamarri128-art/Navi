import os
import shutil
import subprocess


last_search_results = []


# =========================================================
# APPS
# =========================================================

def open_notepad():
    subprocess.Popen("notepad.exe")
    return "Notepad opened."


def open_calculator():
    subprocess.Popen("calc.exe")
    return "Calculator opened."


def open_paint():
    subprocess.Popen("mspaint.exe")
    return "Paint opened."


def open_explorer():
    subprocess.Popen("explorer.exe")
    return "File Explorer opened."


def open_settings():
    subprocess.Popen("start ms-settings:", shell=True)
    return "Settings opened."


def open_cmd():
    subprocess.Popen("cmd.exe")
    return "Command Prompt opened."


def open_chrome():
    chrome_paths = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    ]

    for path in chrome_paths:
        if os.path.exists(path):
            subprocess.Popen(path)
            return "Chrome opened."

    try:
        subprocess.Popen("start chrome", shell=True)
        return "Chrome opened."
    except Exception:
        return "Chrome not found."

    # =========================================================
# MICROSOFT OFFICE
# =========================================================

def open_word():
    try:
        subprocess.Popen("start winword", shell=True)
        return "Microsoft Word opened."
    except Exception:
        return "Microsoft Word not found."


def open_excel():
    try:
        subprocess.Popen("start excel", shell=True)
        return "Microsoft Excel opened."
    except Exception:
        return "Microsoft Excel not found."


def open_powerpoint():
    try:
        subprocess.Popen("start powerpnt", shell=True)
        return "Microsoft PowerPoint opened."
    except Exception:
        return "Microsoft PowerPoint not found."


# =========================================================
# OTHER APPS
# =========================================================

def open_whatsapp():
    try:
        subprocess.Popen("start whatsapp:", shell=True)
        return "WhatsApp opened."
    except Exception:
        return "WhatsApp not found."


def open_telegram():
    try:
        subprocess.Popen("start telegram:", shell=True)
        return "Telegram opened."
    except Exception:
        return "Telegram not found."


def open_edge():
    try:
        subprocess.Popen("start msedge", shell=True)
        return "Microsoft Edge opened."
    except Exception:
        return "Microsoft Edge not found."


def open_spotify():
    try:
        subprocess.Popen("start spotify", shell=True)
        return "Spotify opened."
    except Exception:
        return "Spotify not found."


# =========================================================
# USER LOCATIONS
# =========================================================

def get_user_locations():
    username = os.environ.get("USERNAME")

    if not username:
        return []

    user_path = os.path.join(
        r"C:\Users",
        username
    )

    return [
        os.path.join(user_path, "Desktop"),
        os.path.join(user_path, "Documents"),
        os.path.join(user_path, "Downloads"),
        os.path.join(user_path, "Pictures"),
        os.path.join(user_path, "Videos"),
    ]


# =========================================================
# CREATE FOLDER
# =========================================================

def create_folder(folder_path):
    if not folder_path:
        return "Please tell me the folder name."

    try:
        os.makedirs(
            folder_path,
            exist_ok=True
        )

        return f"Folder created: {folder_path}"

    except Exception as error:
        return f"Could not create folder: {error}"


# =========================================================
# OPEN FOLDER
# =========================================================

def open_folder(folder_path):
    if not folder_path:
        return "Please tell me the folder path."

    if not os.path.exists(folder_path):
        return f"Folder not found: {folder_path}"

    if not os.path.isdir(folder_path):
        return f"Not a folder: {folder_path}"

    try:
        subprocess.Popen(
            ["explorer", os.path.abspath(folder_path)]
        )

        return f"Opened: {folder_path}"

    except Exception as error:
        return f"Could not open folder: {error}"


# =========================================================
# OPEN FILE
# =========================================================

def open_file(file_path):
    if not file_path:
        return "Please tell me the file path."

    if not os.path.exists(file_path):
        return f"File not found: {file_path}"

    try:
        os.startfile(
            os.path.abspath(file_path)
        )

        return f"Opened: {file_path}"

    except Exception as error:
        return f"Could not open file: {error}"


# =========================================================
# FIND FOLDER
# =========================================================

def find_folder(folder_name, search_path="."):
    results = []

    if not folder_name:
        return results

    for root, dirs, files in os.walk(search_path):
        for directory in dirs:

            if directory.lower() == folder_name.lower():
                results.append(
                    os.path.join(
                        root,
                        directory
                    )
                )

                if len(results) >= 10:
                    return results

    return results


# =========================================================
# FIND FILE
# =========================================================

def find_file(file_name, search_path="."):
    results = []

    if not file_name:
        return results

    for root, dirs, files in os.walk(search_path):

        for file in files:

            if file.lower() == file_name.lower():
                results.append(
                    os.path.join(
                        root,
                        file
                    )
                )

                if len(results) >= 10:
                    return results

    return results


# =========================================================
# SEARCH COMMON LOCATIONS
# =========================================================

def search_common_locations(file_name):
    results = []

    if not file_name:
        return results

    locations = get_user_locations()

    for location in locations:

        if not os.path.exists(location):
            continue

        for root, dirs, files in os.walk(location):

            for file in files:

                if file.lower() == file_name.lower():

                    results.append(
                        os.path.join(
                            root,
                            file
                        )
                    )

                    if len(results) >= 10:
                        return results

    return results


# =========================================================
# FIND IMAGE
# =========================================================

def find_image(name):
    global last_search_results

    results = []

    image_extensions = (
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".webp",
        ".bmp"
    )

    locations = get_user_locations()

    for location in locations:

        if not os.path.exists(location):
            continue

        for root, dirs, files in os.walk(location):

            for file in files:

                if not file.lower().endswith(
                    image_extensions
                ):
                    continue

                name_without_extension = os.path.splitext(
                    file
                )[0]

                if (
                    not name
                    or name.lower()
                    in name_without_extension.lower()
                ):

                    full_path = os.path.join(
                        root,
                        file
                    )

                    if full_path not in results:
                        results.append(full_path)

                    if len(results) >= 10:
                        last_search_results = results.copy()
                        return results

    last_search_results = results.copy()

    return results


# =========================================================
# FIND AND OPEN FILE
# =========================================================

def find_and_open_file(file_name):
    global last_search_results

    if not file_name:
        return "Please tell me the file name."

    search_name = file_name.lower().strip()

    results = search_common_locations(
        file_name
    )

    if not results:

        locations = get_user_locations()

        for location in locations:

            if not os.path.exists(location):
                continue

            for root, dirs, files in os.walk(location):

                for file in files:

                    if search_name in file.lower():

                        full_path = os.path.join(
                            root,
                            file
                        )

                        if full_path not in results:
                            results.append(full_path)

                        if len(results) >= 10:
                            break

                if len(results) >= 10:
                    break

            if len(results) >= 10:
                break

    if not results:
        return f"I couldn't find {file_name}."

    last_search_results = results.copy()

    file_path = results[0]

    try:
        os.startfile(
            os.path.abspath(file_path)
        )

        return (
            f"Found: {file_path}\n"
            f"Opened: {os.path.basename(file_path)}"
        )

    except Exception as error:

        return (
            f"Found: {file_path}\n"
            f"Could not open file: {error}"
        )


# =========================================================
# FIND FILE TYPE
# =========================================================

def find_file_type(file_type):
    global last_search_results

    if not file_type:
        return "Please tell me the file type."

    file_type = file_type.lower().strip()

    extensions = {
        "video": (
            ".mp4",
            ".avi",
            ".mkv",
            ".mov",
            ".wmv"
        ),

        "videos": (
            ".mp4",
            ".avi",
            ".mkv",
            ".mov",
            ".wmv"
        ),

        "photo": (
            ".jpg",
            ".jpeg",
            ".png",
            ".gif",
            ".webp",
            ".bmp"
        ),

        "photos": (
            ".jpg",
            ".jpeg",
            ".png",
            ".gif",
            ".webp",
            ".bmp"
        ),

        "image": (
            ".jpg",
            ".jpeg",
            ".png",
            ".gif",
            ".webp",
            ".bmp"
        ),

        "images": (
            ".jpg",
            ".jpeg",
            ".png",
            ".gif",
            ".webp",
            ".bmp"
        ),

        "pdf": (
            ".pdf",
        ),

        "document": (
            ".doc",
            ".docx",
            ".txt",
            ".pdf"
        ),

        "documents": (
            ".doc",
            ".docx",
            ".txt",
            ".pdf"
        )
    }

    allowed_extensions = extensions.get(
        file_type
    )

    if not allowed_extensions:

        return (
            f"I don't know how to search "
            f"for {file_type} files."
        )

    results = []

    locations = get_user_locations()

    for location in locations:

        if not os.path.exists(location):
            continue

        for root, dirs, files in os.walk(location):

            for file in files:

                if file.lower().endswith(
                    allowed_extensions
                ):

                    full_path = os.path.join(
                        root,
                        file
                    )

                    if full_path not in results:
                        results.append(full_path)

                    if len(results) >= 10:
                        break

            if len(results) >= 10:
                break

        if len(results) >= 10:
            break

    if not results:

        return (
            f"I couldn't find any "
            f"{file_type} files."
        )

    last_search_results = results.copy()

    return (
        f"Found {len(results)} {file_type} files:\n"
        + "\n".join(
            f"{index + 1}. {path}"
            for index, path in enumerate(results)
        )
        + "\n\nSay 'open 1', 'open 2', etc."
    )


# =========================================================
# OPEN SEARCH RESULT
# =========================================================

def open_search_result(number):
    global last_search_results

    try:
        number = int(number)

    except (ValueError, TypeError):
        return "Please give a valid result number."

    if (
        number < 1
        or number > len(last_search_results)
    ):
        return f"No file found at number {number}."

    file_path = last_search_results[
        number - 1
    ]

    if not os.path.exists(file_path):
        return f"File no longer exists: {file_path}"

    try:
        os.startfile(
            os.path.abspath(file_path)
        )

        return (
            f"Opened: {os.path.basename(file_path)}\n"
            f"Path: {file_path}"
        )

    except Exception as error:
        return f"Could not open file: {error}"


# =========================================================
# DELETE
# =========================================================

def delete_item(path):
    if not path:
        return "Please tell me what to delete."

    if not os.path.exists(path):
        return f"Not found: {path}"

    try:

        if os.path.isdir(path):
            shutil.rmtree(path)

        else:
            os.remove(path)

        return (
            f"Deleted successfully.\n"
            f"Name: {os.path.basename(path)}\n"
            f"Path: {path}"
        )

    except Exception as error:
        return f"Could not delete: {error}"


# =========================================================
# RENAME
# =========================================================

def rename_item(old_path, new_path):
    if not old_path:
        return "Please tell me what to rename."

    if not new_path:
        return "Please tell me the new name."

    if not os.path.exists(old_path):
        return f"Not found: {old_path}"

    if os.path.exists(new_path):
        return f"Already exists: {new_path}"

    try:

        os.rename(
            old_path,
            new_path
        )

        return (
            f"Renamed successfully.\n"
            f"Old: {old_path}\n"
            f"New: {new_path}"
        )

    except Exception as error:
        return f"Could not rename: {error}"


# =========================================================
# COPY
# =========================================================

def copy_item(source, destination):
    if not source:
        return "Please tell me what to copy."

    if not destination:
        return "Please tell me the destination."

    if not os.path.exists(source):
        return f"Source not found: {source}"

    try:

        if os.path.isdir(source):

            shutil.copytree(
                source,
                destination,
                dirs_exist_ok=True
            )

        else:

            shutil.copy2(
                source,
                destination
            )

        return (
            f"Copied successfully.\n"
            f"From: {source}\n"
            f"To: {destination}"
        )

    except Exception as error:
        return f"Could not copy: {error}"


# =========================================================
# MOVE
# =========================================================

def move_item(source, destination):
    if not source:
        return "Please tell me what to move."

    if not destination:
        return "Please tell me the destination."

    if not os.path.exists(source):
        return f"Source not found: {source}"

    try:

        shutil.move(
            source,
            destination
        )

        return (
            f"Moved successfully.\n"
            f"From: {source}\n"
            f"To: {destination}"
        )

    except Exception as error:
        return f"Could not move: {error}"