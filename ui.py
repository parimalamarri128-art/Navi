import tkinter as tk
from tkinter import scrolledtext


class NaviUI:

    def __init__(self):
        self.root = tk.Tk()

        self.root.title("Navi AI Assistant")
        self.root.geometry("900x650")
        self.root.configure(bg="#121212")

        # Header
        header = tk.Frame(
            self.root,
            bg="#181818",
            height=70
        )
        header.pack(fill=tk.X)
        header.pack_propagate(False)

        title = tk.Label(
            header,
            text="NAVI",
            font=("Segoe UI", 22, "bold"),
            bg="#181818",
            fg="white"
        )
        title.pack(side=tk.LEFT, padx=25)

        status = tk.Label(
            header,
            text="● Online",
            font=("Segoe UI", 11),
            bg="#181818",
            fg="#00ff88"
        )
        status.pack(side=tk.RIGHT, padx=25)

        # Chat
        self.chat_history = scrolledtext.ScrolledText(
            self.root,
            wrap=tk.WORD,
            font=("Segoe UI", 12),
            bg="#1e1e1e",
            fg="white",
            insertbackground="white",
            relief=tk.FLAT,
            state="disabled"
        )
        self.chat_history.pack(
            fill=tk.BOTH,
            expand=True,
            padx=20,
            pady=15
        )

        # Bottom chat area
        bottom = tk.Frame(
            self.root,
            bg="#121212"
        )
        bottom.pack(
            fill=tk.X,
            padx=20,
            pady=(0, 20)
        )

        # Message input
        self.input_box = tk.Entry(
            bottom,
            font=("Segoe UI", 13),
            bg="#1e1e1e",
            fg="white",
            insertbackground="white",
            relief=tk.FLAT
        )

        self.input_box.pack(
            side=tk.LEFT,
            fill=tk.X,
            expand=True,
            ipady=12
        )

        # Put visible placeholder text
        self.input_box.insert(
            0,
            "Type your message..."
        )

        self.input_box.bind(
            "<FocusIn>",
            self.remove_placeholder
        )

        # Send button
        self.send_button = tk.Button(
            bottom,
            text="SEND",
            font=("Segoe UI", 11, "bold"),
            bg="#333333",
            fg="white",
            relief=tk.FLAT,
            padx=20,
            pady=10
        )

        self.send_button.pack(
            side=tk.RIGHT,
            padx=(10, 0)
        )

        # Voice button
        self.voice_button = tk.Button(
            bottom,
            text="🎤",
            font=("Segoe UI", 14),
            bg="#333333",
            fg="white",
            relief=tk.FLAT,
            padx=12,
            pady=7
        )

        self.voice_button.pack(
            side=tk.RIGHT,
            padx=(10, 0)
        )

        # Enter key
        self.input_box.bind(
            "<Return>",
            lambda event: self.send_button.invoke()
        )

    def remove_placeholder(self, event=None):

        if self.input_box.get() == "Type your message...":
            self.input_box.delete(0, tk.END)

    def get_message(self):

        message = self.input_box.get().strip()

        if message == "Type your message...":
            return ""

        return message

    def clear_input(self):

        self.input_box.delete(
            0,
            tk.END
        )

    def add_message(self, sender, message):

        self.chat_history.configure(
            state="normal"
        )

        self.chat_history.insert(
            tk.END,
            f"{sender}: {message}\n\n"
        )

        self.chat_history.configure(
            state="disabled"
        )

        self.chat_history.see(tk.END)

    def run(self):

        self.root.mainloop()