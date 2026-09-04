import customtkinter as ctk

class Transactions(ctk.CTkFrame):
    def __init__(self, parent, controller, fg_color, corner_radius):
        self.controller = controller
        super().__init__(parent, fg_color=fg_color, corner_radius=corner_radius)