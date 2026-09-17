import customtkinter as ctk

from View.Transactions.selector import Selector

class Chart(ctk.CTkFrame):
    def __init__(self, parent, fg_color, corner_radius):
        super().__init__(parent, fg_color=fg_color, corner_radius=corner_radius)

        self.create_options(self)
        self.create_chart(self)



    def create_options(self, parent):
        pass

    def create_chart(self, parent):
        pass
    