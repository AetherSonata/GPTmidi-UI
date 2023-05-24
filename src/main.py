import tkinter as tk
from view.view import View
from controller.controller import Controller

def main():
    root = tk.Tk()
    root.title("AI MIDI Generation")
    root.geometry("800x600")

    view = View(root)
    view.pack(expand=True, fill=tk.BOTH)

    controller = Controller(view)

    root.mainloop()

if __name__ == "__main__":
    main()