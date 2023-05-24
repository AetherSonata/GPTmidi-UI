import tkinter as tk
from tkinter import ttk


class Settings(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.header_frame = tk.Frame(self)
        self.body_frame = tk.Frame(self)
        self.footer_frame = tk.Frame(self)

        self.header_frame.pack(fill=tk.X)
        self.body_frame.pack(expand=True, fill=tk.BOTH)
        self.footer_frame.pack(fill=tk.X, side=tk.BOTTOM)

        label = tk.Label(self.header_frame, text="Settings", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button_frame = tk.Frame(self.header_frame)
        button_frame.pack(side="top", fill="x")


        settings_body = tk.Frame(self.body_frame)
        settings_body.pack(expand=True, fill=tk.BOTH, padx=10, pady=5)

        # Add the settings content
        self.add_setting_entry(settings_body, "Save PATH")
        self.add_setting_entry(settings_body, "Save Filename")
        self.add_setting_entry(settings_body, "Insert Your ChatGPT API KEY", long_text=True)
        self.add_setting_entry(settings_body, "Custom Deep Instruction (Advanced)")

        generate_midi_button = tk.Button(self.footer_frame, text="Go to the start page", command=lambda: controller.show_frame("GPTmidi"))
        upload_example_button = tk.Button(self.footer_frame, text="Load From File")
        generate_midi_button.pack(side=tk.LEFT, padx=10, pady=5)
        upload_example_button.pack(side=tk.RIGHT, padx=10, pady=5)

    def add_setting_entry(self, settings_body, text, long_text=False):
        entry_frame = tk.Frame(settings_body)
        entry_frame.pack(side=tk.TOP, fill=tk.X, pady=5)

        label = tk.Label(entry_frame, text=text, anchor=tk.W)
        label.pack(side=tk.LEFT, padx=5)

        if long_text:
            entry = tk.Text(entry_frame, width=30, height=5)
            entry.pack(side=tk.LEFT, padx=5)
        else:
            entry = tk.Entry(entry_frame)
            entry.pack(side=tk.LEFT, padx=5)

        save_button = tk.Button(entry_frame, text="Save")
        save_button.pack(side=tk.LEFT, padx=5)


