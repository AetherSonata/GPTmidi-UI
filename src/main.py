import tkinter as tk
from view.view import View
from controller import Controller
from model.preference_utils import Preferences

def main():
    root = tk.Tk()
    root.title("AI MIDI Generation")
    root.geometry("800x600")
    
    preferences = Preferences()  
    preferences.write_default_preferences()  # if file does not exist
    loaded_preferences = preferences.load_preferences()  

    view = View(root)
    view.pack(expand=True, fill=tk.BOTH)

    Controller(view, loaded_preferences)

    root.mainloop()

if __name__ == "__main__":
    main()

#for testing conversion:
"""
0 Tempo 500000
0 TimeSig 4/4 24 8
0 NoteOn ch=1 n=60 v=64
240 NoteOff ch=1 n=60 v=64
"""