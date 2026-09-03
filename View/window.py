import customtkinter as ctk

from View.Overview.dashboard import Dashboard
from View.sidebar import Sidebar


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

        self.window_frame = ctk.CTkFrame(self.window, fg_color = "#191c1f", corner_radius=0)
        self.window_frame.pack(fill = "both")

        sidebar = Sidebar(self.window_frame, self.controller, fg_color = "#191c1f")
        sidebar.pack(side = "left", anchor = "n", pady = (70,0), padx = (0,10))
        self.create_overview_dashboard(self.window_frame)

        self.window.mainloop()

    def create_overview_dashboard(self, parent):
        Dashboard(parent, self.controller)        