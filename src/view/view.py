import tkinter as tk
from tkinter import font


class View(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        # Defines the overall button styling
        self.button_font = font.Font(size=12)
        self.button_bg = "lightgray"
        self.button_fg = "black"
        self.button_width = 20
        self.button_height = 2

        self.cp_button_width = 10

        self.label_font = font.Font(size=16)

        self.header_frame = tk.Frame(self)
        self.body_frame = tk.Frame(self)
        self.footer_frame = tk.Frame(self)

        self.header_frame.pack(fill=tk.X, padx=30)
        self.body_frame.pack(expand=True, fill=tk.BOTH)
        self.footer_frame.pack(fill=tk.X, side=tk.BOTTOM, pady=20)

        label = tk.Label(self.header_frame, text="AI MIDI Generation", font=self.label_font)
        label.pack(side="top", fill="x", pady=10)

        button_frame = tk.Frame(self.body_frame, width=int(self.winfo_width() / 4))
        button_frame.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.button_settings = tk.Button(self.footer_frame, text="Settings", font=self.button_font, bg=self.button_bg, fg=self.button_fg, width=self.button_width, height=self.button_height)
        self.button_settings.pack(side="right", pady=5, padx=10)

        self.button_GPTmidi = tk.Button(button_frame, text="Generate from Prompt", font=self.button_font, bg=self.button_bg, fg=self.button_fg, width=self.button_width, height=self.button_height)
        self.button_convert_text_to_midi = tk.Button(button_frame, text="Convert Text to MIDI", font=self.button_font, bg=self.button_bg, fg=self.button_fg, width=self.button_width, height=self.button_height)
        self.button_convert_midi_to_text = tk.Button(button_frame, text="Convert MIDI to Text", font=self.button_font, bg=self.button_bg, fg=self.button_fg, width=self.button_width, height=self.button_height)
        self.button_upload_example_midi = tk.Button(button_frame, text="Upload Example MIDI", font=self.button_font, bg=self.button_bg, fg=self.button_fg, width=self.button_width, height=self.button_height)
        self.button_open_folder = tk.Button(button_frame, text="Open in Folder", font=self.button_font, bg=self.button_bg, fg=self.button_fg, width=self.button_width, height=self.button_height)
        self.button_preview_midi = tk.Button(button_frame, text="Preview MIDI", font=self.button_font, bg=self.button_bg, fg=self.button_fg, width=self.button_width, height=self.button_height)
        self.button_GPTmidi.pack(side="top", pady=5, padx=10)
        self.button_convert_text_to_midi.pack(side="top", pady=5, padx=10)
        self.button_convert_midi_to_text.pack(side="top", pady=5, padx=10)
        self.button_upload_example_midi.pack(side="top", pady=5, padx=10)
        self.button_open_folder.pack(side="top", pady=(50,5), padx=10)
        self.button_preview_midi.pack(side="top", pady=5, padx=10)

        text_frame = tk.Frame(self.body_frame)
        text_frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=20, expand=True)

        self.text_widget = tk.Text(text_frame, state=tk.NORMAL)
        self.text_widget.insert(tk.END, "Input Prompt or MIDI-Text")
        self.text_widget.pack(expand=True, fill=tk.BOTH)

        self.button_clear = tk.Button(self.footer_frame, text="Clear", font=self.button_font, bg=self.button_bg, fg=self.button_fg, width=self.cp_button_width, height=self.button_height)
        self.button_paste = tk.Button(self.footer_frame, text="Paste", font=self.button_font, bg=self.button_bg, fg=self.button_fg, width=self.cp_button_width, height=self.button_height)
        self.button_copy = tk.Button(self.footer_frame, text="Copy", font=self.button_font, bg=self.button_bg, fg=self.button_fg, width=self.cp_button_width, height=self.button_height)
        self.button_clear.pack(side=tk.LEFT, padx=10, pady=5)
        self.button_paste.pack(side=tk.LEFT, padx=10, pady=5)
        self.button_copy.pack(side="left", padx=10, pady=5)

