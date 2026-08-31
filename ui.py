import tkinter as tk
from tkinter import scrolledtext


class NaviUI:

    def __init__(self):

        # ==========================
        # WINDOW
        # ==========================

        self.root = tk.Tk()

        self.root.title("🤖 Navi AI Assistant")

        self.root.geometry("950x700")

        self.root.minsize(850, 600)

        self.root.configure(bg="#0D1117")

        # ==========================
        # HEADER
        # ==========================

        header = tk.Frame(
            self.root,
            bg="#161B22",
            height=85,
            highlightbackground="#30363D",
            highlightthickness=1
        )

        header.pack(fill=tk.X)

        header.pack_propagate(False)

        left = tk.Frame(
            header,
            bg="#161B22"
        )

        left.pack(
            side=tk.LEFT,
            padx=20,
            pady=10
        )

        title = tk.Label(
            left,
            text="🤖 NAVI AI ASSISTANT",
            font=("Segoe UI", 20, "bold"),
            bg="#161B22",
            fg="white"
        )

        title.pack(anchor="w")

        subtitle = tk.Label(
            left,
            text="Powered by Python • Local AI • Windows Automation",
            font=("Segoe UI", 10),
            bg="#161B22",
            fg="#8B949E"
        )

        subtitle.pack(anchor="w")

        self.status = tk.Label(
            header,
            text="🟢 READY",
            font=("Segoe UI", 11, "bold"),
            bg="#161B22",
            fg="#3FB950"
        )

        self.status.pack(
            side=tk.RIGHT,
            padx=20
        )

        # ==========================
        # CHAT AREA
        # ==========================

        self.chat_history = scrolledtext.ScrolledText(
            self.root,
            wrap=tk.WORD,
            font=("Segoe UI", 12),
            bg="#0D1117",
            fg="white",
            insertbackground="white",
            relief=tk.FLAT,
            borderwidth=0,
            state="disabled"
        )

        self.chat_history.pack(
            fill=tk.BOTH,
            expand=True,
            padx=18,
            pady=15
        )

        # ==========================
        # INPUT FRAME
        # ==========================

        bottom = tk.Frame(
            self.root,
            bg="#0D1117"
        )

        bottom.pack(
            fill=tk.X,
            padx=18,
            pady=(0, 12)
        )

        # ==========================
        # INPUT BOX
        # ==========================

        self.input_box = tk.Entry(
            bottom,
            font=("Segoe UI", 13),
            bg="#1F2937",
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

        self.input_box.insert(
            0,
            "Ask Navi anything..."
        )

        self.input_box.bind(
            "<FocusIn>",
            self.remove_placeholder
        )

        self.input_box.bind(
            "<Return>",
            lambda event: self.send_button.invoke()
        )

        # ==========================
        # VOICE BUTTON
        # ==========================

        self.voice_button = tk.Button(
            bottom,
            text="🎤 Speak",
            font=("Segoe UI", 11, "bold"),
            bg="#10B981",
            fg="white",
            activebackground="#059669",
            activeforeground="white",
            relief=tk.FLAT,
            padx=18,
            pady=10,
            cursor="hand2"
        )

        self.voice_button.pack(
            side=tk.RIGHT,
            padx=(10, 0)
        )

        # ==========================
        # SEND BUTTON
        # ==========================

        self.send_button = tk.Button(
            bottom,
            text="📤 Send",
            font=("Segoe UI", 11, "bold"),
            bg="#2563EB",
            fg="white",
            activebackground="#1D4ED8",
            activeforeground="white",
            relief=tk.FLAT,
            padx=18,
            pady=10,
            cursor="hand2"
        )

        self.send_button.pack(
            side=tk.RIGHT,
            padx=(10, 0)
        )

        # ==========================
        # FOOTER
        # ==========================

        self.footer = tk.Label(
            self.root,
            text="Ready",
            bg="#161B22",
            fg="#3FB950",
            font=("Segoe UI", 10),
            anchor="w",
            padx=15,
            pady=6
        )

        self.footer.pack(fill=tk.X)

            # =====================================================
    # REMOVE PLACEHOLDER
    # =====================================================

    def remove_placeholder(self, event=None):

        if self.input_box.get() == "Ask Navi anything...":
            self.input_box.delete(0, tk.END)

    # =====================================================
    # GET MESSAGE
    # =====================================================

    def get_message(self):

        message = self.input_box.get().strip()

        if message == "Ask Navi anything...":
            return ""

        return message

    # =====================================================
    # CLEAR INPUT
    # =====================================================

    def clear_input(self):

        self.input_box.delete(
            0,
            tk.END
        )

    # =====================================================
    # STATUS
    # =====================================================

    def set_status(self, text, color="#3FB950"):

       self.status.config(
          text=text,
          fg=color
    )

       self.footer.config(
          text=text,
          fg=color
    )

       self.root.update_idletasks()

    # =====================================================
    # ADD MESSAGE
    # =====================================================

    def add_message(self, sender, message):

        self.chat_history.configure(state="normal")

        if sender.lower() == "you":

            self.chat_history.insert(
                tk.END,
                "👤 YOU\n",
                "user"
            )

            self.chat_history.insert(
                tk.END,
                message + "\n\n"
            )

        else:

            self.chat_history.insert(
                tk.END,
                "🤖 NAVI\n",
                "bot"
            )

            self.chat_history.insert(
                tk.END,
                message + "\n\n"
            )

        self.chat_history.tag_config(
            "user",
            foreground="#58A6FF",
            font=("Segoe UI", 12, "bold")
        )

        self.chat_history.tag_config(
            "bot",
            foreground="#3FB950",
            font=("Segoe UI", 12, "bold")
        )

        self.chat_history.configure(state="disabled")

        self.chat_history.see(tk.END)

    # =====================================================
    # RUN
    # =====================================================

    def run(self):

        self.root.mainloop()

        