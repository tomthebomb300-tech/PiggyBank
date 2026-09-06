import customtkinter as ctk

from datetime import date
from View.Transactions.date_range_slider import Date_range_slider
from View.Transactions.category_selector import Category_selector

class Transactions(ctk.CTkFrame):
    def __init__(self, parent, controller, fg_color, corner_radius):
        super().__init__(parent, fg_color=fg_color, corner_radius=corner_radius)
        self.controller = controller

        self.start_date = self.controller.getStartDate()
        self.last_date = self.controller.getLastDate()

        slider = Date_range_slider(parent=self,start_date=self.start_date,end_date=self.last_date,command=self.range_changed)
        slider.pack(fill="x", padx=20, pady=20)

        category_selector = Category_selector(parent=self, categories=self.controller.getCategories())
        category_selector.pack()

    def range_changed(self, start, end):
        self.start_date = start
        self.last_date = end
        pass