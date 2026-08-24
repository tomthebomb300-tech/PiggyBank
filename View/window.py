import customtkinter as ctk

from View.Overview.dashboard import Dashboard


class Window:
    def __init__(self, name, height, width, controller):
        self.name = name
        self.height = height
        self.width = width
        self.controller = controller

        self.create_window()

    def create_window(self):
        self.window = ctk.CTk()
        self.window.title("Finaces")
        self.window.geometry("{0}x{1}".format(self.width, self.height))
        self.create_overview_dashboard()
        self.window.mainloop()

    def create_overview_dashboard(self):
        Dashboard(self.window, self.controller)