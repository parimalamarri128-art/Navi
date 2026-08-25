def normalize_text(text):
    return text.strip().lower()


def extract_search_query(text, keywords):
    text = normalize_text(text)

    for keyword in keywords:
        if keyword in text:
            query = text.split(keyword, 1)[1].strip()

            if query:
                return query

    return None


def understand_command(text):

    text = normalize_text(text)

    # =========================
    # Apps
    # =========================

    if "open notepad" in text or "notepad open" in text:
        return {"action": "open_notepad"}

    if "open calculator" in text or "calculator open" in text:
        return {"action": "open_calculator"}

    if "open paint" in text or "paint open" in text:
        return {"action": "open_paint"}

    if (
        "open explorer" in text
        or "file explorer" in text
        or "explorer open" in text
    ):
        return {"action": "open_explorer"}

    if "open settings" in text or "settings open" in text:
        return {"action": "open_settings"}

    if (
        "open cmd" in text
        or "open command prompt" in text
        or "command prompt" in text
    ):
        return {"action": "open_cmd"}

    if "open chrome" in text or "chrome open" in text:
        return {"action": "open_chrome"}

    # =========================
    # Browser
    # =========================

    if "open google" in text or "google open" in text:
        return {"action": "open_google"}

    if "open youtube" in text or "youtube open" in text:
        return {"action": "open_youtube"}

    # =========================
    # Google Search
    # =========================

    google_keywords = [
        "google search",
        "search google",
        "search on google"
    ]

    if any(keyword in text for keyword in google_keywords):

        query = extract_search_query(
            text,
            google_keywords
        )

        if query:
            return {
                "action": "google_search",
                "query": query
            }

    # =========================
    # YouTube Search
    # =========================

    youtube_keywords = [
        "youtube search",
        "search youtube",
        "search on youtube"
    ]

    if any(keyword in text for keyword in youtube_keywords):

        query = extract_search_query(
            text,
            youtube_keywords
        )

        if query:
            return {
                "action": "youtube_search",
                "query": query
            }

            # =========================
    # Natural File Open
    # =========================

    if text.endswith(" file open chey"):

        file_name = text[:-len(" file open chey")].strip()

        if file_name:
            return {
                "action": "find_and_open_file",
                "name": file_name
            }

    if text.endswith(" file ni open chey"):

        file_name = text[:-len(" file ni open chey")].strip()

        if file_name:
            return {
                "action": "find_and_open_file",
                "name": file_name
            }

       # =========================
    # File Type Search
    # =========================

    if text.endswith(" files open chey"):

        file_type = text[:-len(" files open chey")].strip()

        if file_type:
            return {
                "action": "find_file_type",
                "type": file_type
            }

    if text == "documents open chey":
        return {
            "action": "find_file_type",
            "type": "documents"
        }

    if text == "open documents":
        return {
            "action": "find_file_type",
            "type": "documents"
        }
    

            # =========================
    # Open Search Result
    # =========================

    if text.startswith("open "):

        number = text[len("open "):].strip()

        if number.isdigit():
            return {
                "action": "open_search_result",
                "number": int(number)
            }

            # =========================
    # Search and Open File
    # =========================

    if text.endswith(" open chey"):

        file_name = text[:-len(" open chey")].strip()

        if "." in file_name:
            return {
                "action": "find_and_open_file",
                "name": file_name
            }

    if text.endswith(" ni open chey"):

        file_name = text[:-len(" ni open chey")].strip()

        if "." in file_name:
            return {
                "action": "find_and_open_file",
                "name": file_name
            }

    # =========================
    # Open File - English
    # =========================

    if text.startswith("open file "):

        file_path = text[len("open file "):].strip()

        if file_path:
            return {
                "action": "open_file",
                "path": file_path
            }

    if text.startswith("open "):

        possible_file = text[len("open "):].strip()

        if (
            "." in possible_file
            and not possible_file.startswith("http")
        ):
            return {
                "action": "open_file",
                "path": possible_file
            }

    # =========================
    # Open File - Telugu
    # =========================

    if text.endswith(" ni open chey"):

        file_path = text[:-len(" ni open chey")].strip()

        if file_path:
            return {
               "action": "find_and_open_file",
               "name": file_path
            }

    if text.endswith(" ni open cheyyi"):

        file_path = text[:-len(" ni open cheyyi")].strip()

        if file_path:
            return {
               "action": "find_and_open_file",
               "name": file_path
            }

    if text.endswith(" open chey"):

        file_path = text[:-len(" open chey")].strip()

        if file_path:
            return {
               "action": "find_and_open_file",
               "name": file_path
            }

    if text.endswith(" open cheyyi"):

        file_path = text[:-len(" open cheyyi")].strip()

        if file_path:
            return {
               "action": "find_and_open_file",
               "name": file_path
            }

    # =========================
    # Create Folder
    # =========================

    if text.startswith("create folder "):

        folder_name = text[len("create folder "):].strip()

        if folder_name:
            return {
                "action": "create_folder",
                "path": folder_name
            }

    if text.startswith("create a folder "):

        folder_name = text[len("create a folder "):].strip()

        if folder_name:
            return {
                "action": "create_folder",
                "path": folder_name
            }

    # =========================
    # Open Folder
    # =========================

    if text.startswith("open folder "):

        folder_path = text[len("open folder "):].strip()

        if folder_path:
            return {
                "action": "open_folder",
                "path": folder_path
            }

    # =========================
    # Find File
    # =========================

    if text.startswith("find file "):

        file_name = text[len("find file "):].strip()

        if file_name:
            return {
                "action": "find_file",
                "name": file_name
            }

    # =========================
    # Find Folder
    # =========================

    if text.startswith("find folder "):

        folder_name = text[len("find folder "):].strip()

        if folder_name:
            return {
                "action": "find_folder",
                "name": folder_name
            }

    # =========================
    # System
    # =========================

    if (
        "lock pc" in text
        or "lock computer" in text
    ):
        return {"action": "lock_pc"}

    if (
        "task manager" in text
        or "open task manager" in text
    ):
        return {"action": "open_task_manager"}

    if (
        "control panel" in text
        or "open control panel" in text
    ):
        return {"action": "open_control_panel"}

    # =========================
    # Unknown
    # =========================

    return {
        "action": "unknown",
        "text": text
    }