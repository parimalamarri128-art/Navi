import os
import shutil
import subprocess

last_search_results = []


def create_folder(folder_path):
    os.makedirs(folder_path, exist_ok=True)
    return f"Folder created: {folder_path}"



def open_folder(folder_path):
    if not folder_path:
        return "Please tell me the folder name."

    folder_path = folder_path.strip()

    # First: check if it is already a valid path
    if os.path.isdir(folder_path):
        try:
            subprocess.Popen(
                ["explorer", os.path.abspath(folder_path)]
            )
            return f"Opened: {os.path.abspath(folder_path)}"

        except Exception as error:
            return f"Could not open folder: {error}"

    # Search by folder name
    results = find_folder(folder_path)

    if not results:
        return f"Folder not found: {folder_path}"

    # Open the first matching folder
    folder = results[0]

    try:
        subprocess.Popen(
            ["explorer", os.path.abspath(folder)]
        )

        return f"Opened: {folder}"

    except Exception as error:
        return f"Could not open folder: {error}"

def open_file(file_path):
    if not os.path.exists(file_path):
        return f"File not found: {file_path}"

    try:
        os.startfile(os.path.abspath(file_path))
        return f"Opened: {file_path}"

    except Exception as error:
        return f"Could not open file: {error}"


def find_folder(folder_name, search_path=None):
    global last_search_results

    if not folder_name:
        return []

    folder_name = folder_name.lower().strip()

    username = os.environ.get("USERNAME")

    if not username:
        return []

    user_path = os.path.join(
        "C:\\Users",
        username
    )

    # Common Windows folders
    special_folders = {
        "desktop": os.path.join(user_path, "Desktop"),
        "documents": os.path.join(user_path, "Documents"),
        "downloads": os.path.join(user_path, "Downloads"),
        "pictures": os.path.join(user_path, "Pictures"),
        "videos": os.path.join(user_path, "Videos"),
    }

    # Directly check common Windows folders
    if folder_name in special_folders:

        folder_path = special_folders[folder_name]

        if os.path.isdir(folder_path):
            last_search_results = [folder_path]

            return [folder_path]

        return []

    # Search specific path if provided
    if search_path:
        locations = [search_path]

    else:
        locations = [
            os.path.join(user_path, "Desktop"),
            os.path.join(user_path, "Documents"),
            os.path.join(user_path, "Downloads"),
            os.path.join(user_path, "Pictures"),
            os.path.join(user_path, "Videos"),
        ]

    results = []

    for location in locations:

        if not os.path.exists(location):
            continue

        for root, dirs, files in os.walk(location):

            for directory in dirs:

                if directory.lower() == folder_name:

                    results.append(
                        os.path.join(root, directory)
                    )

                    if len(results) >= 10:
                        last_search_results = results.copy()
                        return results

    last_search_results = results.copy()

    return results

def find_file(file_name, search_path="."):
    results = []

    for root, dirs, files in os.walk(search_path):
        for file in files:
            if file.lower() == file_name.lower():
                results.append(
                    os.path.join(root, file)
                )

    return results

def search_common_locations(item_name):

    username = os.environ.get("USERNAME")

    if not username:
        return []

    user_path = os.path.join(
        "C:\\Users",
        username
    )

    locations = [
        os.path.join(user_path, "Desktop"),
        os.path.join(user_path, "Documents"),
        os.path.join(user_path, "Downloads"),
        os.path.join(user_path, "Pictures"),
        os.path.join(user_path, "Videos"),
    ]

    results = []

    item_name = item_name.lower().strip()

    for location in locations:

        if not os.path.exists(location):
            continue

        for root, dirs, files in os.walk(location):

            # Search folders
            for directory in dirs:

                if directory.lower() == item_name:
                    results.append(
                        os.path.join(root, directory)
                    )

            # Search files
            for file in files:

                if file.lower() == item_name:
                    results.append(
                        os.path.join(root, file)
                    )

    return results

def find_image(name):
    global last_search_results

    results = []

    username = os.environ.get("USERNAME")

    if not username:
        return results

    user_path = os.path.join(
        "C:\\Users",
        username
    )

    locations = [
        os.path.join(user_path, "Desktop"),
        os.path.join(user_path, "Documents"),
        os.path.join(user_path, "Downloads"),
        os.path.join(user_path, "Pictures"),
        os.path.join(user_path, "Videos"),
    ]

    image_extensions = (
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".webp",
        ".bmp"
    )

    for location in locations:

        if not os.path.exists(location):
            continue

        for root, dirs, files in os.walk(location):

            for file in files:

                if not file.lower().endswith(image_extensions):
                    continue

                name_without_extension = os.path.splitext(file)[0]

                if (
                    not name
                    or name.lower() in name_without_extension.lower()
                ):
                    results.append(
                        os.path.join(root, file)
                    )

                    if len(results) >= 10:
                        last_search_results = results
                        return results

    last_search_results = results

    return results


def find_and_open_file(file_name):

    search_name = file_name.lower().strip()

    results = search_common_locations(
        file_name
    )

    if not results:

        username = os.environ.get("USERNAME")

        if username:

            user_path = os.path.join(
                "C:\\Users",
                username
            )

            locations = [
                os.path.join(user_path, "Desktop"),
                os.path.join(user_path, "Documents"),
                os.path.join(user_path, "Downloads"),
                os.path.join(user_path, "Pictures"),
                os.path.join(user_path, "Videos"),
            ]

            for location in locations:

                if not os.path.exists(location):
                    continue

                for root, dirs, files in os.walk(location):

                    for file in files:

                        if search_name in file.lower():

                            results.append(
                                os.path.join(root, file)
                            )

    if not results:
        return f"I couldn't find {file_name}."

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


def find_file_type(file_type):
    global last_search_results

    username = os.environ.get("USERNAME")

    if not username:
        return "Could not find user folder."

    user_path = os.path.join(
        "C:\\Users",
        username
    )

    locations = [
        os.path.join(user_path, "Desktop"),
        os.path.join(user_path, "Documents"),
        os.path.join(user_path, "Downloads"),
        os.path.join(user_path, "Pictures"),
        os.path.join(user_path, "Videos"),
    ]

    extensions = {
        "video": [
            ".mp4",
            ".avi",
            ".mkv",
            ".mov",
            ".wmv"
        ],
        "videos": [
            ".mp4",
            ".avi",
            ".mkv",
            ".mov",
            ".wmv"
        ],
        "photo": [
            ".jpg",
            ".jpeg",
            ".png",
            ".gif",
            ".webp",
            ".bmp"
        ],
        "photos": [
            ".jpg",
            ".jpeg",
            ".png",
            ".gif",
            ".webp",
            ".bmp"
        ],
        "image": [
            ".jpg",
            ".jpeg",
            ".png",
            ".gif",
            ".webp",
            ".bmp"
        ],
        "images": [
            ".jpg",
            ".jpeg",
            ".png",
            ".gif",
            ".webp",
            ".bmp"
        ],
        "pdf": [
            ".pdf"
        ],

        "python": [
    ".py"
     ],

        "document": [
            ".doc",
            ".docx",
            ".txt",
            ".pdf"
        ],
        "documents": [
            ".doc",
            ".docx",
            ".txt",
            ".pdf"
        ]
    }

    allowed_extensions = extensions.get(
        file_type.lower(),
        []
    )

    if not allowed_extensions:
        return f"I don't know how to search for {file_type} files."

    results = []

    for location in locations:

        if not os.path.exists(location):
            continue

        for root, dirs, files in os.walk(location):

            for file in files:

                if file.lower().endswith(
                    tuple(allowed_extensions)
                ):

                    results.append(
                        os.path.join(root, file)
                    )

                    if len(results) >= 10:
                        break

            if len(results) >= 10:
                break

        if len(results) >= 10:
            break

    if not results:
        return f"I couldn't find any {file_type} files."

    last_search_results = results.copy()

    return (
        f"Found {len(results)} {file_type} files:\n"
        + "\n".join(
            f"{index + 1}. {path}"
            for index, path in enumerate(results)
        )
    )


def open_search_result(number):

    if number < 1 or number > len(last_search_results):
        return f"No file found at number {number}."

    file_path = last_search_results[number - 1]

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
# DELETE FILE SEARCH
# =========================================================

pending_delete = None


def find_and_delete_file(file_name):

    global pending_delete

    if not file_name:
        return "Please tell me the file name."

    results = search_common_locations(file_name)

    if not results:

        username = os.environ.get("USERNAME")

        if username:

            user_path = os.path.join(
                "C:\\Users",
                username
            )

            locations = [
                os.path.join(user_path, "Desktop"),
                os.path.join(user_path, "Documents"),
                os.path.join(user_path, "Downloads"),
                os.path.join(user_path, "Pictures"),
                os.path.join(user_path, "Videos"),
            ]

            for location in locations:

                if not os.path.exists(location):
                    continue

                for root, dirs, files in os.walk(location):

                    for file in files:

                        if file_name.lower() in file.lower():

                            results.append(
                                os.path.join(root, file)
                            )

                            break

                    if results:
                        break

                if results:
                    break

    if not results:
        return f"I couldn't find {file_name}."

    pending_delete = results[0]

    return (
        f"I found:\n{pending_delete}\n\n"
        "Are you sure you want to delete it?\n"
        "Reply with yes or no."
    )


# =========================================================
# CONFIRM DELETE
# =========================================================

def confirm_delete(answer):

    global pending_delete

    if not pending_delete:
        return "There is no file waiting for deletion."

    answer = answer.lower().strip()

    if answer in (
        "yes",
        "y",
        "avunu",
        "haa",
        "ha"
    ):

        path = pending_delete

        pending_delete = None

        return delete_item(path)

    elif answer in (
        "no",
        "n",
        "vaddu",
        "ledu"
    ):

        pending_delete = None

        return "Delete cancelled."

    return "Please reply with yes or no."


# =========================================================
# DELETE FILE / FOLDER
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
            f"Deleted: {os.path.basename(path)}\n"
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
            "Renamed successfully.\n"
            f"Old: {old_path}\n"
            f"New: {new_path}"
        )

    except Exception as error:

        return f"Could not rename: {error}"


# =========================================================
# COPY
# =========================================================

def copy_item(source, destination):

    if not os.path.exists(source):
        return f"Source not found: {source}"

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

    return f"Copied to: {destination}"


# =========================================================
# MOVE
# =========================================================

def move_item(source, destination):

    if not os.path.exists(source):
        return f"Source not found: {source}"

    shutil.move(
        source,
        destination
    )

    return f"Moved to: {destination}"

def find_and_rename_file(old_name, new_name):

    if not old_name:
        return "Please tell me the item to rename."

    if not new_name:
        return "Please tell me the new name."

    results = search_common_locations(old_name)

    if not results:
        return f"I couldn't find {old_name}."

    old_path = results[0]

    try:

        new_path = os.path.join(
            os.path.dirname(old_path),
            new_name
        )

        if os.path.exists(new_path):
            return f"Already exists: {new_path}"

        os.rename(
            old_path,
            new_path
        )

        item_type = "Folder" if os.path.isdir(new_path) else "File"

        return (
            f"{item_type} renamed successfully.\n"
            f"Old: {old_path}\n"
            f"New: {new_path}"
        )

    except Exception as error:

        return f"Could not rename: {error}"

def find_and_copy_file(item_name, destination):

    if not item_name:
        return "Please tell me what to copy."

    if not destination:
        return "Please tell me where to copy it."

    results = search_common_locations(item_name)

    if not results:
        return f"I couldn't find {item_name}."

    source = results[0]

    username = os.environ.get("USERNAME")

    if not username:
        return "Could not find user folder."

    destination_lower = destination.lower().strip()

    if destination_lower == "desktop":
        destination = os.path.join(
            "C:\\Users",
            username,
            "Desktop"
        )

    elif destination_lower == "documents":
        destination = os.path.join(
            "C:\\Users",
            username,
            "Documents"
        )

    elif destination_lower == "downloads":
        destination = os.path.join(
            "C:\\Users",
            username,
            "Downloads"
        )

    elif destination_lower == "pictures":
        destination = os.path.join(
            "C:\\Users",
            username,
            "Pictures"
        )

    elif destination_lower == "videos":
        destination = os.path.join(
            "C:\\Users",
            username,
            "Videos"
        )

    destination = os.path.abspath(destination)

    try:

        os.makedirs(
            destination,
            exist_ok=True
        )

        target = os.path.join(
            destination,
            os.path.basename(source)
        )

        if os.path.exists(target):
            return f"Already exists: {target}"

        if os.path.isdir(source):

            shutil.copytree(
                source,
                target
            )

        else:

            shutil.copy2(
                source,
                target
            )

        item_type = "Folder" if os.path.isdir(source) else "File"

        return f"{item_type} copied to: {target}"

    except Exception as error:

        return f"Could not copy: {error}"

def find_and_move_file(item_name, destination):

    if not item_name:
        return "Please tell me what to move."

    if not destination:
        return "Please tell me where to move it."

    results = search_common_locations(item_name)

    if not results:
        return f"I couldn't find {item_name}."

    source = results[0]

    username = os.environ.get("USERNAME")

    if not username:
        return "Could not find user folder."

    destination_lower = destination.lower().strip()

    if destination_lower == "desktop":
        destination = os.path.join(
            "C:\\Users",
            username,
            "Desktop"
        )

    elif destination_lower == "documents":
        destination = os.path.join(
            "C:\\Users",
            username,
            "Documents"
        )

    elif destination_lower == "downloads":
        destination = os.path.join(
            "C:\\Users",
            username,
            "Downloads"
        )

    elif destination_lower == "pictures":
        destination = os.path.join(
            "C:\\Users",
            username,
            "Pictures"
        )

    elif destination_lower == "videos":
        destination = os.path.join(
            "C:\\Users",
            username,
            "Videos"
        )

    destination = os.path.abspath(destination)

    try:

        os.makedirs(
            destination,
            exist_ok=True
        )

        target = os.path.join(
            destination,
            os.path.basename(source)
        )

        if os.path.exists(target):
            return f"Already exists: {target}"

        shutil.move(
            source,
            target
        )

        item_type = "Folder" if os.path.isdir(target) else "File"

        return f"{item_type} moved to: {target}"

    except Exception as error:

        return f"Could not move: {error}"

def create_file(file_path):
    if not file_path:
        return "Please tell me the file name."

    try:
        username = os.environ.get("USERNAME")

        if not username:
            return "Could not find user folder."

        if not os.path.isabs(file_path):
            file_path = os.path.join(
                "C:\\Users",
                username,
                "Documents",
                file_path
            )

        file_path = os.path.abspath(file_path)

        if os.path.exists(file_path):
            return f"File already exists: {file_path}"

        os.makedirs(
            os.path.dirname(file_path),
            exist_ok=True
        )

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:
            file.write("")

        return f"File created: {file_path}"

    except Exception as error:
        return f"Could not create file: {error}"


def find_and_rename_file(old_name, new_name):
    if not old_name:
        return "Please tell me the file to rename."

    if not new_name:
        return "Please tell me the new name."

    results = search_common_locations(old_name)

    if not results:
        return f"I couldn't find {old_name}."

    old_path = results[0]

    try:
        new_path = os.path.join(
            os.path.dirname(old_path),
            new_name
        )

        if os.path.exists(new_path):
            return f"Already exists: {new_path}"

        os.rename(old_path, new_path)

        return (
            f"Renamed successfully.\n"
            f"Old: {old_path}\n"
            f"New: {new_path}"
        )

    except Exception as error:
        return f"Could not rename file: {error}"


def find_and_copy_file(file_name, destination):
    if not file_name:
        return "Please tell me what to copy."

    if not destination:
        return "Please tell me where to copy it."

    results = search_common_locations(file_name)

    if not results:
        return f"I couldn't find {file_name}."

    source = results[0]

    username = os.environ.get("USERNAME")

    if destination.lower() == "desktop":
        destination = os.path.join(
            "C:\\Users",
            username,
            "Desktop"
        )

    elif destination.lower() == "documents":
        destination = os.path.join(
            "C:\\Users",
            username,
            "Documents"
        )

    elif destination.lower() == "downloads":
        destination = os.path.join(
            "C:\\Users",
            username,
            "Downloads"
        )

    elif destination.lower() == "pictures":
        destination = os.path.join(
            "C:\\Users",
            username,
            "Pictures"
        )

    destination = os.path.abspath(destination)

    try:
        os.makedirs(
            destination,
            exist_ok=True
        )

        target = os.path.join(
            destination,
            os.path.basename(source)
        )

        if os.path.isdir(source):
            shutil.copytree(
                source,
                target,
                dirs_exist_ok=True
            )
        else:
            shutil.copy2(
                source,
                target
            )

        return f"Copied to: {target}"

    except Exception as error:
        return f"Could not copy: {error}"


def find_and_move_file(file_name, destination):
    if not file_name:
        return "Please tell me what to move."

    if not destination:
        return "Please tell me where to move it."

    results = search_common_locations(file_name)

    if not results:
        return f"I couldn't find {file_name}."

    source = results[0]

    username = os.environ.get("USERNAME")

    if destination.lower() == "desktop":
        destination = os.path.join(
            "C:\\Users",
            username,
            "Desktop"
        )

    elif destination.lower() == "documents":
        destination = os.path.join(
            "C:\\Users",
            username,
            "Documents"
        )

    elif destination.lower() == "downloads":
        destination = os.path.join(
            "C:\\Users",
            username,
            "Downloads"
        )

    elif destination.lower() == "pictures":
        destination = os.path.join(
            "C:\\Users",
            username,
            "Pictures"
        )

    destination = os.path.abspath(destination)

    try:
        os.makedirs(
            destination,
            exist_ok=True
        )

        target = os.path.join(
            destination,
            os.path.basename(source)
        )

        shutil.move(
            source,
            target
        )

        return f"Moved to: {target}"

    except Exception as error:
        return f"Could not move: {error}"

   