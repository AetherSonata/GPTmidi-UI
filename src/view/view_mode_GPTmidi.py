import tkinter as tk


class GPTmidi(tk.Frame):
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

        button1 = tk.Button(button_frame, text="Text to MIDI", command=lambda: controller.show_frame("Text_to_Midi"))
        button2 = tk.Button(button_frame, text="MIDI to Text", command=lambda: controller.show_frame("Midi_to_Text"))
        button3 = tk.Button(button_frame, text="Settings", command=lambda: controller.show_frame("Settings"))
        button1.pack(side="left", padx=10, pady=5)
        button2.pack(side="left", padx=10, pady=5)
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