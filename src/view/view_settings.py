import tkinter as tk
from tkinter import font
from model.preference_utils import Preferences


class SettingsView(tk.Frame):
    def __init__(self, parent, preferences):
        tk.Frame.__init__(self, parent)
        self.preferences = preferences
        self.label_font = font.Font(size=16)

        self.header_frame = tk.Frame(self)
        self.body_frame = tk.Frame(self)
        self.footer_frame = tk.Frame(self)

        self.header_frame.pack(fill=tk.X, padx=30)
        self.body_frame.pack(expand=True, fill=tk.BOTH)
        self.footer_frame.pack(fill=tk.X, side=tk.BOTTOM, pady=20)

        label = tk.Label(self.header_frame, text="Settings", font=self.label_font)
        label.pack(side="top", fill="x", pady=10)

        preference_keys = ["save_folder", "file_name", "API_KEY"]
        self.entry_vars = []
        self.new_items = []

        for key in preference_keys:
            description_frame = tk.Frame(self.body_frame)
            description_frame.pack(fill=tk.X, pady=5, padx=20)

            description_label = tk.Label(description_frame, text=key, anchor=tk.W, width=25)
            description_label.pack(side=tk.LEFT)

            description_entry = tk.Entry(description_frame)
            description_entry.pack(side=tk.RIGHT, padx=10)

            self.entry_vars.append(tk.StringVar())

            if key in self.preferences:
                self.entry_vars[-1].set(self.preferences[key])

            self.new_items.append(description_entry)

        checkbox_frame = tk.Frame(self.body_frame)
        checkbox_frame.pack(fill=tk.X, padx=20)

        auto_show_checkbox = tk.Checkbutton(checkbox_frame, text="Auto Show", font=self.label_font)
        auto_show_checkbox.pack(side=tk.LEFT, padx=10, pady=5)

        button_frame = tk.Frame(self.body_frame)
        button_frame.pack(fill=tk.X, padx=20)

        instructions_button = tk.Button(button_frame, text="Edit Instructions", font=self.label_font,
                                        command=lambda: handle_edit_instructions())
        instructions_button.pack(side=tk.LEFT, padx=0, pady=5)

        save_exit_button = tk.Button(self.footer_frame, text="Save & Exit", font=self.label_font,
                                    command=lambda: handle_save_and_exit())
        save_exit_button.pack(side=tk.LEFT, padx=10, pady=5)

        back_button = tk.Button(self.footer_frame, text="Back", font=self.label_font,
                                command=lambda: handle_back())
        back_button.pack(side=tk.LEFT, padx=10, pady=5)

        def handle_edit_instructions():
            print("edit instruction pressed")

        def handle_save_and_exit():
            import json
            print("save and exit pressed")

            # Create a dictionary to store the updated preferences
            new_preferences = {}

            # Iterate over the entry variables and new items
            for entry_var, new_item in zip(self.entry_vars, self.new_items):
                key = new_item.cget("text")  # Get the key from the label's text
                value = entry_var.get()  # Get the updated value from the entry variable

        def handle_save_and_exit():
            print("save and exit pressed")

            # Create a dictionary to store the updated preferences
            new_preferences = {}

            # Iterate over the entry variables and new items
            for entry_var, new_item in zip(self.entry_vars, self.new_items):
                key = new_item.cget("text")  # Get the key from the label's text
                value = entry_var.get()  # Get the updated value from the entry variable

                new_preferences[key] = value

            # Create an instance of the Preferences class
            preferences = Preferences()

            # Load the existing preferences from the file
            preferences.load_preferences()

            # Get the original preferences
            original_preferences = preferences.load_preferences()

            # Update the new_preferences dictionary with the unchanged values from original_preferences
            for key, value in original_preferences.items():
                if key not in new_preferences:
                    new_preferences[key] = value

            # Update the values if they have changed
            new_preferences["save_folder"] = ".\\output"  # Hardcoded save folder
            new_preferences["file_name"] = "output"  # Hardcoded file name
            new_preferences["API_KEY"] = "insert your OpenAI API-KEY here"  # Hardcoded API key
            new_preferences["auto_show_created_file_in_folder"] = new_preferences.get("auto_show_created_file_in_folder", False)

            # Write the updated preferences to a file
            preferences.write_new_preferences(new_preferences)

            self.master.destroy()

        def handle_back():
            print("back pressed")
            self.master.destroy()

        for entry, entry_var in zip(self.new_items, self.entry_vars):
            entry.configure(textvariable=entry_var)
