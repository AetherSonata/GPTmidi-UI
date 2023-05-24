import tkinter as tk


class Text_to_Midi(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.header_frame = tk.Frame(self)
        self.body_frame = tk.Frame(self)
        self.footer_frame = tk.Frame(self)

        self.header_frame.pack(fill=tk.X)
        self.body_frame.pack(expand=True, fill=tk.BOTH)
        self.footer_frame.pack(fill=tk.X, side=tk.BOTTOM)

        label = tk.Label(self.header_frame, text="Midi Converted Successfully", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button_frame = tk.Frame(self.header_frame)
        button_frame.pack(side="top", fill="x")

        button = tk.Button(button_frame, text="Go to the start page", command=lambda: controller.show_frame("StartPage"))
        button.pack(side="left", padx=10, pady=5)

        text_widget = tk.Text(self.body_frame, state=tk.NORMAL)
        text_widget.insert(tk.END, "insert midi text here")
        text_widget.configure(state=tk.DISABLED)
        text_widget.pack(expand=True, fill=tk.BOTH)

        generate_midi_button = tk.Button(self.footer_frame, text="Convert to MIDI", command=lambda: controller.show_frame("Processed_Text"))
        upload_example_button = tk.Button(self.footer_frame, text="Upload Example")
        generate_midi_button.pack(side=tk.LEFT, padx=10, pady=5)
        upload_example_button.pack(side=tk.LEFT, padx=10, pady=5)
