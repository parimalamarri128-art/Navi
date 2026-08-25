import os
import webbrowser

from app_manager import (
    open_notepad,
    open_calculator,
    open_paint,
    open_explorer,
    open_settings,
    open_cmd,
    open_chrome,
)

from intent_manager import detect_intent

from browser_manager import (
    open_google,
    open_youtube,
    google_search,
    youtube_search,
)

from file_manager import (
    create_folder,
    create_file,
    delete_item,
    open_folder,
    open_file,
    find_file,
    find_folder,
    find_image,
    find_and_open_file,
    find_file_type,
    open_search_result,
    find_and_delete_file,
    confirm_delete,
    find_and_rename_file,
    find_and_copy_file,
    find_and_move_file,
)

from system_manager import (
    lock_pc,
    open_task_manager,
    open_control_panel,
)

from ai import understand_command
from voice import VoiceManager
from ui import NaviUI


class Navi:

    def __init__(self):
        self.voice = VoiceManager()
        self.ui = NaviUI()

        self.ui.send_button.config(
            command=self.process_text_command
        )

        self.ui.voice_button.config(
            command=self.process_voice_command
        )

    def execute_command(self, command):

        action = command.get("action")

        # =====================================================
        # APPS
        # =====================================================

        if action == "open_notepad":
            open_notepad()
            return "Notepad opened."

        elif action == "open_calculator":
            open_calculator()
            return "Calculator opened."

        elif action == "open_paint":
            open_paint()
            return "Paint opened."

        elif action == "open_explorer":
            open_explorer()
            return "File Explorer opened."

        elif action == "open_settings":
            open_settings()
            return "Settings opened."

        elif action == "open_cmd":
            open_cmd()
            return "Command Prompt opened."

        elif action == "open_chrome":
            open_chrome()
            return "Chrome opened."

        # =====================================================
        # BROWSER
        # =====================================================

        elif action == "open_google":
            open_google()
            return "Google opened."

        elif action == "open_youtube":
            open_youtube()
            return "YouTube opened."

        elif action == "open_website":
            url = command.get("url", "")

            if not url:
                return "Website URL not found."

            webbrowser.open(url)
            return "Website opened."

        elif action == "google_search":
            query = command.get("query", "")

            if not query:
                return "What should I search on Google?"

            google_search(query)
            return f"Searching Google for {query}"

        elif action == "youtube_search":
            query = command.get("query", "")

            if not query:
                return "What should I search on YouTube?"

            youtube_search(query)
            return f"Searching YouTube for {query}"

              # =========================================================
        # FILE MANAGER
        # =========================================================

        elif action == "create_folder":
            path = command.get("path", "")

            if not path:
                return "Please tell me the folder name."

            return create_folder(path)

        elif action == "open_folder":
            path = command.get("path", "")

            if not path:
                return "Please tell me the folder path."

            return open_folder(path)

        elif action == "open_file":
            path = command.get("path", "")

            if not path:
                return "Please tell me the file path."

            return open_file(path)

        elif action == "find_and_open_file":
            name = command.get("name", "")

            if not name:
                return "Please tell me the file name."

            return find_and_open_file(name)

        elif action == "find_image":
            name = command.get("name", "")

            results = find_image(name)

            if not results:
                if name:
                    return f"I couldn't find image {name}."

                return "I couldn't find any images."

            return (
                f"Found {len(results)} images:\n"
                + "\n".join(
                    f"{i + 1}. {path}"
                    for i, path in enumerate(results)
                )
                + "\n\nSay 'open 1', 'open 2', etc."
            )

        elif action == "find_file_type":
            file_type = command.get("type", "")

            if not file_type:
                return "Please tell me the file type."

            return find_file_type(file_type)

        elif action == "open_search_result":
            number = command.get("number", 0)

            if not number:
                return "Please tell me the result number."

            return open_search_result(number)

        elif action == "find_file":
            name = command.get("name", "")

            if not name:
                return "Please tell me the file name."

            results = find_file(name)

            if not results:
                return f"I couldn't find {name}."

            return (
                "Found:\n"
                + "\n".join(results[:5])
            )

        elif action == "find_folder":
            name = command.get("name", "")

            if not name:
                return "Please tell me the folder name."

            results = find_folder(name)

            if not results:
                return f"I couldn't find the folder {name}."

            return (
                "Found:\n"
                + "\n".join(results[:5])
            )

        # =========================================================
        # DELETE
        # =========================================================

        elif action == "find_and_delete_file":
            name = command.get("name", "")

            if not name:
                return "Please tell me the file name."

            return find_and_delete_file(name)

        elif action == "confirm_delete":
            answer = command.get("answer", "")

            return confirm_delete(answer)

        elif action == "delete_item":
            path = command.get("path", "")

            if not path:
                return "Please tell me what to delete."

            return delete_item(path)

        # =========================================================
        # CREATE FILE
        # =========================================================

        elif action == "create_file":
            path = command.get("path", "")

            if not path:
                return "Please tell me the file name."

            return create_file(path)
    

        # =========================================================
        # RENAME
        # =========================================================

        elif action == "rename_item":
            old_path = command.get("old_path", "")
            new_path = command.get("new_path", "")

            if not old_path:
                return "Please tell me what to rename."

            if not new_path:
                return "Please tell me the new name."

            return find_and_rename_file(
                old_path,
                new_path
            )

        # =========================================================
        # COPY
        # =========================================================

        elif action == "copy_item":
            source = command.get("source", "")
            destination = command.get("destination", "")

            if not source:
                return "Please tell me what to copy."

            if not destination:
                return "Please tell me where to copy it."

            return find_and_copy_file(
                source,
                destination
            )

        # =========================================================
        # MOVE
        # =========================================================

        elif action == "move_item":
            source = command.get("source", "")
            destination = command.get("destination", "")

            if not source:
                return "Please tell me what to move."

            if not destination:
                return "Please tell me where to move it."

            return find_and_move_file(
                source,
                destination
            )

        # =========================================================
        # SYSTEM
        # =========================================================

        elif action == "lock_pc":
            lock_pc()
            return "PC locked."

        elif action == "open_task_manager":
            open_task_manager()
            return "Task Manager opened."

        elif action == "open_control_panel":
            open_control_panel()
            return "Control Panel opened."

            # =========================================================
        # UNKNOWN
        # =========================================================

        else:
            return "Sorry, I don't understand that command yet."

    def process_command(self, text):

        if not text:
            return

        intent = detect_intent(text)

        if intent:
            command = intent
        else:
            command = understand_command(text)

        response = self.execute_command(command)

        self.ui.add_message(
            "Navi",
            response
        )

        self.voice.speak(response)


    def process_text_command(self):

        text = self.ui.get_message()

        if not text:
            return

        self.ui.clear_input()

        self.ui.add_message(
            "You",
            text
        )

        self.process_command(text)


    def process_voice_command(self):

        text = self.voice.listen()

        if not text:
            return

        self.ui.add_message(
            "You",
            text
        )

        self.process_command(text)


    def start(self):

        self.ui.add_message(
            "Navi",
            "Hello! I am Navi. How can I help you?"
        )

        self.voice.speak(
            "Hello! I am Navi. How can I help you?"
        )

        self.ui.run()


if __name__ == "__main__":
    navi = Navi()
    navi.start()