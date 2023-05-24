import tkinter as tk
from view.view import View
from controller import Controller

def main():
    root = tk.Tk()
    root.title("AI MIDI Generation")
    root.geometry("800x600")
    
#ToDo create function for loading preferences from file at Startup
    preferences = {
    "save_folder": ".\output",
    "file_name": "output"
}

    view = View(root)
    view.pack(expand=True, fill=tk.BOTH)

    controller = Controller(view, preferences)

    root.mainloop()

if __name__ == "__main__":
    main()