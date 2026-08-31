import os
import json

REMINDER_FILE = "reminders.json"


def load_reminders():
    if not os.path.exists(REMINDER_FILE):
        return []

    with open(REMINDER_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_reminders(reminders):
    with open(REMINDER_FILE, "w", encoding="utf-8") as f:
        json.dump(reminders, f, indent=4)


def create_reminder(task, time):
    reminders = load_reminders()

    reminders.append({
        "task": task,
        "time": time
    })

    save_reminders(reminders)

    return f"Reminder '{task}' saved for {time}."


def show_reminders():
    reminders = load_reminders()

    if not reminders:
        return "No reminders found."

    result = "Reminders:\n"

    for r in reminders:
        result += f"{r['time']} - {r['task']}\n"

    return result


def delete_reminder(task):
    reminders = load_reminders()

    new_list = [r for r in reminders if r["task"].lower() != task.lower()]

    if len(new_list) == len(reminders):
        return "Reminder not found."

    save_reminders(new_list)

    return f"Reminder '{task}' deleted."

from datetime import datetime


def get_due_reminders():
    reminders = load_reminders()

    now = datetime.now().strftime("%I %p").lower()

    due = []

    for reminder in reminders:
        if reminder["time"].lower() == now:
            due.append(reminder)

    return due