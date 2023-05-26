import tkinter as tk
from view.view import View
from controller import Controller
from model.settings import Preferences

def main():
    root = tk.Tk()
    root.title("AI MIDI Generation")
    root.geometry("800x600")
    
    Preferences.write_default_preferences()
    preferences = Preferences.load_preferences()

    view = View(root)
    view.pack(expand=True, fill=tk.BOTH)

    controller = Controller(view, preferences)

    root.mainloop()

if __name__ == "__main__":
    main()