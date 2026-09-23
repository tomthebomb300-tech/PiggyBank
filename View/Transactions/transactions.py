import customtkinter as ctk

from View.Transactions.search import Search

class Transactions(ctk.CTkFrame):
    def __init__(self, parent, controller, fg_color, corner_radius):
        super().__init__(parent, fg_color=fg_color, corner_radius=corner_radius)
        self.controller = controller

        search = Search(self, controller, fg_color=fg_color, corner_radius=corner_radius)
        search.pack(side = "bottom", fill = "both", expand = True, pady = (30,15), padx = 15)
