class Controller:
    def __init__(self, start_page, app):
        self.start_page = start_page
        self.app = app
        self.add_event_handlers()

    def add_event_handlers(self):
        self.start_page.button1.config(command=lambda: self.app.show_frame("Text_to_Midi"))
        self.start_page.button2.config(command=self.button2_clicked)

    def button1_clicked(self):
        print("Button 1 clicked")

    def button2_clicked(self):
        print("Button 2 clicked")
