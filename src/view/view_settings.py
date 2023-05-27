import tkinter as tk
from tkinter import font

class SettingsView(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.label_font = font.Font(size=16)

        self.header_frame = tk.Frame(self)
        self.body_frame = tk.Frame(self)
        self.footer_frame = tk.Frame(self)

        self.header_frame.pack(fill=tk.X, padx=30)
        self.body_frame.pack(expand=True, fill=tk.BOTH)
        self.footer_frame.pack(fill=tk.X, side=tk.BOTTOM, pady=20)

        label = tk.Label(self.header_frame, text="Settings", font=self.label_font)
        label.pack(side="top", fill="x", pady=10)

        description_texts = [
            "Save Folder:",
            "File Name:",
            "API Key:"
        ]

        self.descriptions = []
        self.new_items = []

        for text in description_texts:
            description_frame = tk.Frame(self.body_frame)
            description_frame.pack(fill=tk.X, pady=5, padx=20)

            description_label = tk.Label(description_frame, text=text, anchor=tk.W, width=25)
            description_label.pack(side=tk.LEFT)

            description_entry = tk.Entry(description_frame)
            description_entry.pack(side=tk.RIGHT, padx=10)

            self.descriptions.append(description_label)
            self.new_items.append(description_entry)
            
        checkbox_frame = tk.Frame(self.body_frame)
        checkbox_frame.pack(fill=tk.X, padx=20)
        
        auto_show_checkbox = tk.Checkbutton(checkbox_frame, text="Auto Show", font=self.label_font)
        auto_show_checkbox.pack(side=tk.LEFT, padx=10, pady=5)
        
        button_frame = tk.Frame(self.body_frame)
        button_frame.pack(fill=tk.X, padx=20)

        instructions_button = tk.Button(button_frame, text="Edit Instructions", font=self.label_font, command=lambda: edit_instructions() )
        instructions_button.pack(side=tk.LEFT, padx=0, pady=5)        

        save_exit_button = tk.Button(self.footer_frame, text="Save & Exit", font=self.label_font, command=lambda: save_and_exit())
        save_exit_button.pack(side=tk.LEFT, padx=10, pady=5)

        back_button = tk.Button(self.footer_frame, text="Back", font=self.label_font)
        back_button.pack(side=tk.LEFT, padx=10, pady=5)

        def edit_instructions():
            print("edit istruction pressed")

        def save_and_exit():
            print("save and exit pressed")
            self.master.destroy()            