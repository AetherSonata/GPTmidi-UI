import os
import subprocess
from model.text_to_midi_converter import convert_text_to_midi
from model.midi_utils import play_midi
import tkinter.messagebox as messagebox
import tkinter as tk
from tkinter import font

class Controller:
    def __init__(self, view, preferences):
        self.view = view
        self.preferences = preferences
        self.output_path = None

        # Assign handler functions to buttons
        self.view.button_settings.config(command=self.handle_settings)
        self.view.button_GPTmidi.config(command=self.handle_generate_from_prompt)
        self.view.button_convert_text_to_midi.config(command=self.handle_convert_text_to_midi)
        self.view.button_convert_midi_to_text.config(command=self.handle_convert_midi_to_text)
        self.view.button_upload_example_midi.config(command=self.handle_upload_example_midi)
        self.view.button_clear.config(command=self.handle_clear)
        self.view.button_paste.config(command=self.handle_paste)
        self.view.button_copy.config(command=self.handle_copy)
        self.view.button_open_folder.config(command=self.handle_open_in_folder)
        self.view.button_preview_midi.config(command=self.handle_preview_midi)

    def handle_settings(self):
        # Add code to handle settings button click here
        print("Settings button clicked")

    def handle_generate_from_prompt(self):
        # Add code to handle generate from prompt button click here
        print("Generate from Prompt button clicked")

    def handle_convert_text_to_midi(self):
        # Add code to handle convert text to MIDI button click here
        self.view.text_widget.tag_add("sel", "1.0", "end")
        sel_start = self.view.text_widget.index("sel.first")
        sel_end = self.view.text_widget.index("sel.last")

        if sel_start and sel_end:
            text = self.view.text_widget.get(sel_start, sel_end)
            file_name = self.preferences["file_name"]
            save_folder = self.preferences["save_folder"]

            file_number = 1
            while os.path.exists(os.path.join(save_folder, f"{file_name}{file_number}.mid")):
                file_number += 1

            output_filename = f"{file_name}{file_number}.mid"
            output_path = os.path.join(save_folder, output_filename)

            if not os.path.exists(save_folder):
                os.makedirs(save_folder)

            self.output_path = output_path

            convert_text_to_midi(text, output_path)
            print("File saved:", output_path)
        else:
            print("No text selected or selection is empty.")

        print("Convert Text to MIDI button clicked")

    def handle_convert_midi_to_text(self):
        # Add code to handle convert MIDI to text button click here
        print("Convert MIDI to Text button clicked")

    def handle_upload_example_midi(self):
        # Add code to handle upload example MIDI button click here
        print("Upload Example MIDI button clicked")

    def handle_clear(self):
        # Add code to handle clear button click here
        self.view.text_widget.delete("1.0", tk.END)
        print("Clear button clicked")

    def handle_paste(self):
        # Add code to handle paste button click here
        clipboard_text = self.view.clipboard_get()
        self.view.text_widget.delete("1.0", tk.END)
        self.view.text_widget.insert("1.0", clipboard_text)
        print("Paste button clicked")

    def handle_copy(self):
        # Add code to handle copy button click here
        self.view.text_widget.tag_add("sel", "1.0", "end")
        selected_text = self.view.text_widget.get("sel.first", "sel.last")
        if selected_text:
            self.view.clipboard_clear()
            self.view.clipboard_append(selected_text)
            print("Copy button clicked")
        else:
            messagebox.showinfo("Error", "No text selected.")

    def handle_open_in_folder(self):
        # Add code to open and select the last created file in the folder if existent
        if self.output_path and os.path.exists(self.output_path):
            subprocess.Popen(f'explorer /select,"{self.output_path}"')
        else:
            print("Output path not found.")

    def handle_preview_midi(self):
        # Add code to handle preview MIDI button click here
        if self.output_path and os.path.exists(self.output_path):
            play_midi(self.output_path)
            print("Previewing MIDI:", self.output_path)
        else:
            print("Output path not found.")

    def get_output_path(self):
        return self.output_path

    def set_output_path(self, output_path):
        self.output_path = output_path
