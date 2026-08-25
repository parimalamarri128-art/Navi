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
    # YOUTUBE SMART SEARCH
    # =========================================================

    youtube_words = [
        "song",
        "songs",
        "trailer",
        "movie"
    ]

    if any(
        word in original_text
        for word in youtube_words
    ):
        return {
            "action": "youtube_search",
            "query": original_text
        }

       # =========================================================
    # GOOGLE SMART SEARCH
    # =========================================================

    google_words = [
        "tutorial",
        "how to",
        "meaning",
        "news",
        "weather"
    ]

    if any(
        word in original_text
        for word in google_words
    ):
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
    # UNKNOWN
    # =========================================================

    return None