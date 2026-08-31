import keyboard


def play_pause():
    keyboard.send("play/pause media")
    return "Play/Pause executed."


def next_song():
    keyboard.send("next track")
    return "Next song."


def previous_song():
    keyboard.send("previous track")
    return "Previous song."


def stop_music():
    keyboard.send("stop media")
    return "Music stopped."