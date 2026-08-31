import os
import webbrowser
import threading

import time
from datetime import datetime

from app_manager import (
    open_notepad,
    open_calculator,
    open_paint,
    open_explorer,
    open_settings,
    open_cmd,
    open_chrome,
    open_word,
    open_excel,
    open_powerpoint,
    open_whatsapp,
    open_telegram,
    open_edge,
    open_spotify,
)

from ai_chat import ask_ai

from intent_manager import detect_intent

from developer_manager import (
    open_vscode,
    open_pycharm,
    open_visual_studio,
    open_android_studio,
    open_intellij,
    open_eclipse,
    open_terminal,
    open_cmd,
    open_powershell,
    check_python,
    check_git,
    check_node,
    check_java,
)

from it_manager import (
    check_cpu,
    check_ram,
    check_disk,
    system_information,
    windows_version,
    show_ip,
    open_device_manager,
    open_services,
    open_event_viewer,
)

from hardware_manager import (
    battery_information,
    bios_information,
    gpu_information,
    storage_information,
    usb_devices,
    motherboard_information,
)

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

from volume_manager import (
    volume_up,
    volume_down,
    mute_volume,
    unmute_volume,
)

from screenshot_manager import take_screenshot

from brightness_manager import (
    brightness_up,
    brightness_down,
    set_brightness,
    get_brightness,
)

from notes_manager import (
    create_note,
    show_notes,
    open_note,
    delete_note,
)

from reminder_manager import (
    create_reminder,
    show_reminders,
    delete_reminder,
    get_due_reminders,
)

from media_manager import (
    play_pause,
    next_song,
    previous_song,
    stop_music,
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
# MORE APPLICATIONS
# =====================================================

        elif action == "open_word":
           return open_word()

        elif action == "open_excel":
           return open_excel()

        elif action == "open_powerpoint":
           return open_powerpoint()

        elif action == "open_whatsapp":
           return open_whatsapp()

        elif action == "open_telegram":
           return open_telegram()

        elif action == "open_edge":
           return open_edge()

        elif action == "open_spotify":
           return open_spotify()


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

        # =====================================================
# VOLUME
# =====================================================

        elif action == "volume_up":
          return volume_up()

        elif action == "volume_down":
           return volume_down()

        elif action == "mute_volume":
           return mute_volume()

        elif action == "unmute_volume":
           return unmute_volume()

        # =====================================================
# SCREENSHOT
# =====================================================

        elif action == "take_screenshot":
           return take_screenshot()

        # =====================================================
# BRIGHTNESS
# =====================================================

        elif action == "brightness_up":
           return brightness_up()

        elif action == "brightness_down":
           return brightness_down()

        elif action == "get_brightness":
           return get_brightness()

        elif action == "set_brightness":
           level = command.get("level", 50)
           return set_brightness(level)

        # =====================================================
# NOTES
# =====================================================

        elif action == "create_note":
           name = command.get("name", "")
           return create_note(name)

        elif action == "show_notes":
           return show_notes()

        elif action == "open_note":
           name = command.get("name", "")
           return open_note(name)

        elif action == "delete_note":
           name = command.get("name", "")
           return delete_note(name)

        # =====================================================
# REMINDERS
# =====================================================

        elif action == "create_reminder":
           task = command.get("task", "")
           time = command.get("time", "")
           return create_reminder(task, time)

        elif action == "show_reminders":
           return show_reminders()

        elif action == "delete_reminder":
           task = command.get("task", "")
           return delete_reminder(task)

        # =====================================================
# MEDIA CONTROLS
# =====================================================

        elif action == "play_pause":
           return play_pause()

        elif action == "next_song":
           return next_song()

        elif action == "previous_song":
           return previous_song()

        elif action == "stop_music":
           return stop_music()


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
        # DEVELOPER
        # =========================================================

        elif action == "open_vscode":
            return open_vscode()

        elif action == "open_pycharm":
            return open_pycharm()

        elif action == "open_visual_studio":
            return open_visual_studio()

        elif action == "open_android_studio":
            return open_android_studio()

        elif action == "open_intellij":
            return open_intellij()

        elif action == "open_eclipse":
            return open_eclipse()

        elif action == "open_terminal":
            return open_terminal()

        elif action == "open_powershell":
            return open_powershell()

        elif action == "check_python":
            return check_python()

        elif action == "check_git":
            return check_git()

        elif action == "check_node":
            return check_node()

        elif action == "check_java":
            return check_java()
        
                # =========================================================
        # IT SUPPORT MODE
        # =========================================================

        elif action == "check_cpu":
            return check_cpu()

        elif action == "check_ram":
            return check_ram()

        elif action == "check_disk":
            return check_disk()

        elif action == "system_information":
            return system_information()

        elif action == "windows_version":
            return windows_version()

        elif action == "show_ip":
            return show_ip()

        elif action == "open_device_manager":
            return open_device_manager()

        elif action == "open_services":
            return open_services()

        elif action == "open_event_viewer":
            return open_event_viewer()

                # =========================================================
        # HARDWARE MODE
        # =========================================================

        elif action == "battery_information":
            return battery_information()

        elif action == "bios_information":
            return bios_information()

        elif action == "gpu_information":
            return gpu_information()

        elif action == "storage_information":
            return storage_information()

        elif action == "usb_devices":
            return usb_devices()

        elif action == "motherboard_information":
            return motherboard_information()

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

              # =====================================================
        # AI CHAT FALLBACK
        # =====================================================

        if command.get("action") == "unknown":

            threading.Thread(
                target=self.ai_background,
                args=(text,),
                daemon=True
            ).start()

            return

        # =====================================================
        # NORMAL NAVI COMMAND
        # =====================================================

        response = self.execute_command(command)

        self.ui.add_message(
            "Navi",
            response
        )

        self.voice.speak(response)

    def ai_background(self, text):

        response = ask_ai(text)

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

        self.ui.set_status(
            "🤖 Thinking...",
            "#3B82F6"
        )

        self.process_command(text)

        self.ui.set_status(
            "🟢 Ready",
            "#3FB950"
        )

    def process_voice_command(self):

        self.ui.set_status(
            "🎤 Listening...",
            "#F59E0B"
        )

        text = self.voice.listen()

        if not text:

            self.ui.set_status(
                "🟢 Ready",
                "#3FB950"
            )
            return

        self.ui.add_message(
            "You",
            text
        )

        self.ui.set_status(
            "🤖 Thinking...",
            "#3B82F6"
        )

        self.process_command(text)

        self.ui.set_status(
            "🟢 Ready",
            "#3FB950"
        )

    def start(self):

        self.voice.speak(
            "Hello! I am Navi. How can I help you?"
        )

        self.ui.run()


if __name__ == "__main__":
    navi = Navi()
    navi.start()