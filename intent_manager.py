from difflib import SequenceMatcher


# =========================================================
# WEBSITES
# =========================================================

WEBSITES = {
    "chatgpt": "https://chat.openai.com",
    "gmail": "https://mail.google.com",
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "github": "https://github.com",
    "linkedin": "https://www.linkedin.com",
    "facebook": "https://www.facebook.com",
    "instagram": "https://www.instagram.com",
    "amazon": "https://www.amazon.in",
    "netflix": "https://www.netflix.com",
    "spotify": "https://open.spotify.com",
}


def detect_intent(text):

    text = text.lower().strip()

    print("DEBUG TEXT:", repr(text))

    original_text = text

    # =========================================================
    # WEBSITE
    # =========================================================

    website_text = text

    if website_text.startswith("open "):
        website_text = website_text[len("open "):].strip()

    if website_text.endswith(" open chey"):
        website_text = website_text[:-len(" open chey")].strip()

    if website_text in WEBSITES:
        return {
            "action": "open_website",
            "url": WEBSITES[website_text]
        }

        # =========================================================
    # FOLDER SEARCH / OPEN
    # =========================================================

    if text.startswith("find folder "):

        folder_name = text[len("find folder "):].strip()

        if folder_name:
            return {
                "action": "find_folder",
                "name": folder_name
            }

    if text.startswith("open folder "):

        folder_name = text[len("open folder "):].strip()

        if folder_name:
            return {
                "action": "open_folder",
                "path": folder_name
            }

    if text.startswith("find my ") and text.endswith(" folder"):

        folder_name = text[len("find my "):-len(" folder")].strip()

        if folder_name:
            return {
                "action": "find_folder",
                "name": folder_name
            }

        # =========================================================
# APPLICATIONS
# =========================================================

    if text == "open word":
     return {"action": "open_word"}

    elif text == "open excel":
       return {"action": "open_excel"}

    elif text == "open powerpoint":
       return {"action": "open_powerpoint"}

    elif text == "open whatsapp":
        return {"action": "open_whatsapp"}

    elif text == "open telegram":
       return {"action": "open_telegram"}

    elif text == "open edge":
       return {"action": "open_edge"}

    elif text == "open spotify app":
       return {"action": "open_spotify"}

    # =========================================================
# VOLUME
# =========================================================

    if text in ("volume up", "increase volume"):
       return {"action": "volume_up"}

    elif text in ("volume down", "decrease volume"):
       return {"action": "volume_down"}

    elif text == "mute":
       return {"action": "mute_volume"}

    elif text == "unmute":
       return {"action": "unmute_volume"}

    # =========================================================
# BRIGHTNESS
# =========================================================

    if text in ("brightness up", "increase brightness"):
      return {"action": "brightness_up"}

    elif text in ("brightness down", "decrease brightness"):
       return {"action": "brightness_down"}

    elif text == "current brightness":
      return {"action": "get_brightness"}

    elif text.startswith("set brightness to "):
       level = text.replace("set brightness to ", "").replace("%", "").strip()

       if level.isdigit():
        return {
            "action": "set_brightness",
            "level": int(level)
        }

    # =========================================================
# SCREENSHOT
# =========================================================

    if text in (
       "take screenshot",
       "capture screen",
       "take screen shot",
  ):
     return {
        "action": "take_screenshot"
    }

    # =========================================================
# NOTES
# =========================================================

    if text.startswith("create note "):
     return {
        "action": "create_note",
        "name": text.replace("create note ", "").strip()
    }

    elif text == "show my notes":
       return {
        "action": "show_notes"
    }

    elif text.startswith("open note "):
       return {
        "action": "open_note",
        "name": text.replace("open note ", "").strip()
    }

    elif text.startswith("delete note "):
       return {
        "action": "delete_note",
        "name": text.replace("delete note ", "").strip()
    }

    # =========================================================
# REMINDERS
# =========================================================
    if text.startswith("set reminder "):

       reminder = text[len("set reminder "):]

       if " at " in reminder:
            task, time = reminder.rsplit(" at ", 1)

            return {
               "action": "create_reminder",
               "task": task.strip(),
               "time": time.strip()
        }

    elif text == "show reminders":

       return {
           "action": "show_reminders"
    }

    elif text.startswith("delete reminder "):

       task = text[len("delete reminder "):].strip()

       return {
          "action": "delete_reminder",
          "task": task
    }

    # =========================================================
# MEDIA CONTROLS
# =========================================================

    if text in ("play", "pause", "play music", "pause music"):
       return {"action": "play_pause"}

    elif text in ("next song", "next music"):
       return {"action": "next_song"}
 
    elif text in ("previous song", "previous music", "last song"):
       return {"action": "previous_song"}

    elif text in ("stop music", "stop song"):
         return {"action": "stop_music"}

    # =========================================================
    # MY PHOTOS
    # =========================================================

    if text in (
        "my photo",
        "my photos",
        "open my photo",
        "open my photos",
        "find my photo",
        "find my photos",
        "show my photo",
        "show my photos",
    ):
        return {
            "action": "find_image",
            "name": ""
        }

    # =========================================================
    # MY VIDEOS
    # =========================================================

    if text in (
        "my video",
        "my videos",
        "open my video",
        "open my videos",
        "find my video",
        "find my videos",
        "show my video",
        "show my videos",
    ):
        return {
            "action": "find_file_type",
            "type": "videos"
        }

    # =========================================================
    # IMAGE SEARCH BY NAME
    #
    # Examples:
    # parimala photo
    # parimala photos
    # open parimala photo
    # open panda photo
    # =========================================================

    image_name = ""

    if text.startswith("open ") and text.endswith(" photo"):
        image_name = text[len("open "):]
        image_name = image_name[:-len(" photo")].strip()

    elif text.startswith("open ") and text.endswith(" photos"):
        image_name = text[len("open "):]
        image_name = image_name[:-len(" photos")].strip()

    elif text.endswith(" photo"):
        image_name = text[:-len(" photo")].strip()

    elif text.endswith(" photos"):
        image_name = text[:-len(" photos")].strip()

    if image_name:
        return {
            "action": "find_image",
            "name": image_name
        }

    # =========================================================
    # IMAGE FILE NAME
    #
    # Examples:
    # panda.png
    # photo.jpg
    # parimala.jpeg
    # =========================================================

    image_extensions = (
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".webp",
        ".bmp"
    )

    if text.endswith(image_extensions):

        image_name = text.rsplit(".", 1)[0].strip()

        return {
            "action": "find_image",
            "name": image_name
        }

    # =========================================================
    # COMMON IMAGE NAMES
    # =========================================================

    if text in (
        "panda",
        "parimala",
        "photo",
        "image"
    ):
        return {
            "action": "find_image",
            "name": text
        }

        # =========================================================
    # OPEN FILE BY NAME
    #
    # Examples:
    # Parimala_Portfolio.pdf open chey
    # main.py open chey
    # app_manager.py open chey
    # resume.pdf open chey
    # =========================================================

    if text.endswith(" open chey"):

        file_name = text[:-len(" open chey")].strip()

        # Remove "open" if user says:
        # open main.py open chey
        if file_name.startswith("open "):
            file_name = file_name[len("open "):].strip()

        if file_name:
            return {
                "action": "find_and_open_file",
                "name": file_name
            }

    # =========================================================
    # SMART LOCAL FILE SEARCH
    # =========================================================

    file_words = [
        "resume",
        "portfolio",
        "document"
    ]

    if (
        text.startswith("open my ")
        or text.startswith("find my ")
    ):

        file_name = text

        if file_name.startswith("open my "):
            file_name = file_name[len("open my "):].strip()

        elif file_name.startswith("find my "):
            file_name = file_name[len("find my "):].strip()

        # Remove plural words

        file_name = file_name.replace(" photos", "")
        file_name = file_name.replace(" videos", "")
        file_name = file_name.replace(" documents", "")
        file_name = file_name.replace(" images", "")

        # =====================================================
        # Common spelling mistakes
        # =====================================================

        replacements = {
            "ressume": "resume",
            "resum": "resume",
            "resme": "resume",

            "portfoloi": "portfolio",
            "portfoilo": "portfolio",
            "portifolio": "portfolio",
            "portpolio": "portfolio",
            "portolio": "portfolio",
        }

        if file_name in replacements:
            file_name = replacements[file_name]

        # =====================================================
        # Fuzzy matching
        # =====================================================

        best_match = None
        best_score = 0

        for word in file_words:

            score = SequenceMatcher(
                None,
                file_name,
                word
            ).ratio()

            if score > best_score:
                best_score = score
                best_match = word

        if best_match and best_score >= 0.60:

            return {
                "action": "find_and_open_file",
                "name": best_match
            }

    # =========================================================
    # RESUME
    # =========================================================

    if text in (
        "find my resume",
        "open my resume",
        "my resume",
        "find resume",
        "open resume",
        "open my ressume",
        "find my ressume",
        "open my resum",
        "find my resum"
    ):
        return {
            "action": "find_and_open_file",
            "name": "resume"
        }

    # =========================================================
    # PORTFOLIO
    # =========================================================

    if text in (
        "open my portfolio",
        "open my portfoloi",
        "open my portfoilo",
        "open my portifolio",
        "open my portpolio",
        "open my portolio",

        "find my portfolio",
        "find my portfoloi",
        "find my portfoilo",

        "my portfolio"
    ):
        return {
            "action": "find_and_open_file",
            "name": "portfolio"
        }

    # =========================================================
    # DOCUMENT SEARCH
    # =========================================================

    if text in (
        "my documents",
        "my document",
        "find my documents",
        "find my document",
        "open my documents",
        "open my document"
    ):
        return {
            "action": "find_file_type",
            "type": "documents"
        }

    # =========================================================
    # PDF SEARCH
    # =========================================================

    if text in (
        "my pdf",
        "my pdfs",
        "find my pdf",
        "find my pdfs",
        "open my pdf",
        "open my pdfs"
    ):
        return {
            "action": "find_file_type",
            "type": "pdf"
        }

        # =========================================================
    # PYTHON FILE SEARCH
    # =========================================================

    if text in (
        "find python files",
        "find python file",
        "find my python files",
        "show python files",
        "show python file"
    ):
        return {
            "action": "find_file_type",
            "type": "python"
        }

        # =========================================================
    # SMART FILE TYPE SEARCH
    # =========================================================

    if text in (
        "find pdf",
        "find pdfs",
        "find pdf files",
        "find my pdf files",
        "show pdf",
        "show pdfs",
        "show pdf files",
        "show my pdf files"
    ):
        return {
            "action": "find_file_type",
            "type": "pdf"
        }

    if text in (
        "find images",
        "find image files",
        "find my images",
        "find my image files",
        "show images",
        "show image files",
        "show my images"
    ):
        return {
            "action": "find_file_type",
            "type": "images"
        }

    if text in (
        "find documents",
        "find document files",
        "find my document files",
        "show documents",
        "show document files",
        "show my documents"
    ):
        return {
            "action": "find_file_type",
            "type": "documents"
        }

    if text in (
        "find videos",
        "find video files",
        "find my video files",
        "show videos",
        "show video files",
        "show my videos"
    ):
        return {
            "action": "find_file_type",
            "type": "videos"
        }

         # =========================================================
    # YOUTUBE SMART SEARCH
    # =========================================================

    youtube_query = None

    # YouTube patterns
    if original_text.startswith("youtube search "):
        youtube_query = original_text[len("youtube search "):].strip()

    elif original_text.startswith("search youtube "):
        youtube_query = original_text[len("search youtube "):].strip()

    elif original_text.startswith("youtube lo "):
        youtube_query = original_text[len("youtube lo "):].strip()

    # Telugu-English: "... youtube lo vetuku"
    elif " youtube lo " in original_text:
        youtube_query = original_text.split(" youtube lo ", 1)[0].strip()

    # Clean ending words
    if youtube_query:
        youtube_query = youtube_query.replace(
            " search cheyyi", ""
        ).replace(
            " search chey", ""
        ).replace(
            " vetuku", ""
        ).strip()

        if youtube_query:
            return {
                "action": "youtube_search",
                "query": youtube_query
            }

            # =========================================================
    # NATURAL YOUTUBE SEARCH
    # =========================================================

    if " on youtube" in original_text:
        youtube_query = original_text.split(" on youtube", 1)[0].strip()

        if youtube_query.startswith("find "):
            youtube_query = youtube_query[len("find "):].strip()

        if youtube_query:
            return {
                "action": "youtube_search",
                "query": youtube_query
            }

    # =========================================================
    # GOOGLE SMART SEARCH
    # =========================================================

    google_patterns = [
        "google search ",
        "search google ",
        "search "
    ]

    google_query = None

    for pattern in google_patterns:
        if original_text.startswith(pattern):
            google_query = original_text[len(pattern):].strip()
            break

    if google_query:
        return {
            "action": "google_search",
            "query": google_query
        }

    # Smart Google keywords
    google_words = [
        "tutorial",
        "how to",
        "meaning",
        "news",
        "weather"
    ]

    if any(word in original_text for word in google_words):
        return {
            "action": "google_search",
            "query": original_text
        }
    
    # =========================================================
    # DELETE FILE / FOLDER
    # =========================================================

    if original_text.startswith("delete "):

        delete_name = original_text[len("delete "):].strip()

        if not delete_name:
            return {
                "action": "find_and_delete_file",
                "name": ""
            }

        return {
            "action": "find_and_delete_file",
            "name": delete_name
        }

    # =========================================================
    # CONFIRM DELETE
    # =========================================================

    if original_text in (
        "yes",
        "y",
        "avunu",
        "haa",
        "ha"
    ):
        return {
            "action": "confirm_delete",
            "answer": "yes"
        }

    if original_text in (
        "no",
        "n",
        "vaddu",
        "ledu"
    ):
        return {
            "action": "confirm_delete",
            "answer": "no"
        }

    
    # =========================================================
    # CREATE FILE
    # =========================================================

    if original_text.startswith("create file "):

        file_name = original_text[len("create file "):].strip()

        if not file_name:
            return {
                "action": "create_file",
                "path": ""
            }

        return {
            "action": "create_file",
            "path": file_name
        }


        # =========================================================
    # RENAME
    # =========================================================

    if original_text.startswith("rename ") and " to " in original_text:

        data = original_text[len("rename "):].strip()

        old_name, new_name = data.split(" to ", 1)

        return {
            "action": "rename_item",
            "old_path": old_name.strip(),
            "new_path": new_name.strip()
        }

    # =========================================================
    # COPY
    # =========================================================

    if original_text.startswith("copy ") and " to " in original_text:

        data = original_text[len("copy "):].strip()

        source, destination = data.split(" to ", 1)

        return {
            "action": "copy_item",
            "source": source.strip(),
            "destination": destination.strip()
        }

    # =========================================================
    # MOVE
    # =========================================================

    if original_text.startswith("move ") and " to " in original_text:

        data = original_text[len("move "):].strip()

        source, destination = data.split(" to ", 1)

        return {
            "action": "move_item",
            "source": source.strip(),
            "destination": destination.strip()
        }

        # =========================================================
    # DEVELOPER MODE
    # =========================================================

    if text in (
        "open vscode",
        "open vs code",
        "start vscode",
        "start vs code"
    ):
        return {
            "action": "open_vscode"
        }

    if text in (
        "open pycharm",
        "start pycharm"
    ):
        return {
            "action": "open_pycharm"
        }

    if text in (
        "open visual studio",
        "start visual studio"
    ):
        return {
            "action": "open_visual_studio"
        }

    if text in (
        "open android studio",
        "start android studio"
    ):
        return {
            "action": "open_android_studio"
        }

    if text in (
        "open intellij",
        "open intellij idea",
        "start intellij"
    ):
        return {
            "action": "open_intellij"
        }

    if text in (
        "open eclipse",
        "start eclipse"
    ):
        return {
            "action": "open_eclipse"
        }

    if text in (
        "open terminal",
        "start terminal",
        "open windows terminal"
    ):
        return {
            "action": "open_terminal"
        }

    if text in (
        "open powershell",
        "start powershell"
    ):
        return {
            "action": "open_powershell"
        }

    if text in (
        "check python",
        "check python version",
        "python version"
    ):
        return {
            "action": "check_python"
        }

    if text in (
        "check git",
        "check git version",
        "git version"
    ):
        return {
            "action": "check_git"
        }

    if text in (
        "check node",
        "check node version",
        "node version"
    ):
        return {
            "action": "check_node"
        }

    if text in (
        "check java",
        "check java version",
        "java version"
    ):
        return {
            "action": "check_java"
        }

        # =========================================================
    # IT SUPPORT MODE
    # =========================================================

    if text in (
        "check cpu",
        "cpu usage",
        "cpu information"
    ):
        return {
            "action": "check_cpu"
        }

    if text in (
        "check ram",
        "ram usage",
        "ram information",
        "memory usage"
    ):
        return {
            "action": "check_ram"
        }


    if text in (
        "system information",
        "system info",
        "pc information",
        "pc info"
    ):
        return {
            "action": "system_information"
        }

    if text in (
        "windows version",
        "check windows version"
    ):
        return {
            "action": "windows_version"
        }

    if text in (
        "show ip",
        "show ip address",
        "check ip",
        "ip address"
    ):
        return {
            "action": "show_ip"
        }

    if text in (
        "open device manager",
        "device manager"
    ):
        return {
            "action": "open_device_manager"
        }

    if text in (
        "open services",
        "services"
    ):
        return {
            "action": "open_services"
        }

    if text in (
        "open event viewer",
        "event viewer"
    ):
        return {
            "action": "open_event_viewer"
        }

        # =========================================================
    # HARDWARE MODE
    # =========================================================

    if text in (
        "battery information",
        "battery info",
        "check battery",
        "battery"
    ):
        return {
            "action": "battery_information"
        }

    if text in (
        "bios information",
        "bios info",
        "check bios",
        "bios"
    ):
        return {
            "action": "bios_information"
        }

    if text in (
        "gpu information",
        "gpu info",
        "check gpu",
        "display information",
        "graphics information"
    ):
        return {
            "action": "gpu_information"
        }

    if text in (
        "storage information",
        "storage info",
        "check storage",
        "disk information",
        "drive information"
    ):
        return {
            "action": "storage_information"
        }

    if text in (
        "usb devices",
        "usb device",
        "check usb",
        "usb information"
    ):
        return {
            "action": "usb_devices"
        }

    if text in (
        "motherboard information",
        "motherboard info",
        "check motherboard",
        "motherboard"
    ):
        return {
            "action": "motherboard_information"
        }

    # =========================================================
    # UNKNOWN
    # =========================================================

    return None