import os

# Notes folder
NOTES_FOLDER = os.path.join(os.getcwd(), "Notes")
os.makedirs(NOTES_FOLDER, exist_ok=True)


def create_note(name):
    path = os.path.join(NOTES_FOLDER, f"{name}.txt")

    if os.path.exists(path):
        return "Note already exists."

    with open(path, "w", encoding="utf-8") as f:
        f.write("")

    return f"Note '{name}' created."


def show_notes():
    files = [f[:-4] for f in os.listdir(NOTES_FOLDER) if f.endswith(".txt")]

    if not files:
        return "No notes found."

    return "Notes:\n" + "\n".join(files)


def open_note(name):
    path = os.path.join(NOTES_FOLDER, f"{name}.txt")

    if not os.path.exists(path):
        return "Note not found."

    os.startfile(path)
    return f"Opened note '{name}'."


def delete_note(name):
    path = os.path.join(NOTES_FOLDER, f"{name}.txt")

    if not os.path.exists(path):
        return "Note not found."

    os.remove(path)
    return f"Deleted note '{name}'."