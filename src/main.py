import tkinter as tk
from tkinter import font as tkfont
from view.view_mode_gptmidi import GPTmidi
from view.view_mode_midi_to_text import Midi_to_Text
from view.view_settings import Settings
from view.view_processed_text import Processed_Text
from view.view_mode_text_to_midi import Text_to_Midi
from controller.controller import Controller


class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Settings, Processed_Text, Text_to_Midi, Midi_to_Text, GPTmidi):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        self.header_frame = tk.Frame(self)
        self.body_frame = tk.Frame(self)
        self.footer_frame = tk.Frame(self)

        self.header_frame.pack(fill=tk.X)
        self.body_frame.pack(expand=True, fill=tk.BOTH)
        self.footer_frame.pack(fill=tk.X, side=tk.BOTTOM)

        label = tk.Label(self.header_frame, text="AI midi Generation", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button_frame = tk.Frame(self.header_frame)
        button_frame.pack(side="top", fill="x")

        self.button1 = tk.Button(button_frame, text="Text to MIDI")
        self.button2 = tk.Button(button_frame, text="MIDI to Text", command=lambda: controller.show_frame("Midi_to_Text"))
        button3 = tk.Button(button_frame, text="Settings", command=lambda: controller.show_frame("Settings"))
        self.button1.pack(side="left", padx=10, pady=5)
        self.button2.pack(side="left", padx=10, pady=5)
        button3.pack(side="right", padx=10, pady=5)

        text_widget = tk.Text(self.body_frame, state=tk.NORMAL)
        text_widget.insert(tk.END, "Input Text Field")
        text_widget.pack(expand=True, fill=tk.BOTH)

        generate_midi_button = tk.Button(self.footer_frame, text="Generate MIDI", command=lambda: controller.show_frame("Processed_Text") )
        upload_example_button = tk.Button(self.footer_frame, text="Upload Example")
        change_instruction_button = tk.Button(self.footer_frame, text="Change Instruction")
        generate_midi_button.pack(side=tk.LEFT, padx=10, pady=5)
        upload_example_button.pack(side=tk.LEFT, padx=10, pady=5)
        change_instruction_button.pack(side="right", padx=10, pady=5)



if __name__ == "__main__":
    app = SampleApp()

    controller = Controller(app.frames["StartPage"], app)

    app.mainloop()