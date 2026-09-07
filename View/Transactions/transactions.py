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

        slider_fetch_frame = ctk.CTkFrame(self, fg_color="transparent")
        slider_fetch_frame.pack(fill = "x", padx = 20, pady = 20)
        slider_fetch_frame.grid_columnconfigure(0, weight=1)
        slider_fetch_frame.grid_columnconfigure(1, weight=0)

        slider = Date_range_slider(parent=slider_fetch_frame,start_date=self.start_date,end_date=self.last_date,command=self.range_changed)
        slider.grid(row = 0, column = 0, sticky = "ew", padx=20, pady=20)

        fetch_button = ctk.CTkButton(slider_fetch_frame, text="Fetch", command=self.fetch)
        fetch_button.grid(row = 0, column = 1, sticky = "ns", padx = 20, pady = 20)

        self.category_selector = Category_selector(parent=self, categories=self.controller.getCategories(), corner_radius=40)
        self.category_selector.pack(anchor = "w", padx=40, pady=(0,40), fill = "y")
        

    def range_changed(self, start, end):
        self.start_date = start
        self.last_date = end

    def fetch(self):
        income_expense = self.controller.getIncomeExpense(self.category_selector.get_selected(), self.start_date, self.last_date)
        for key in income_expense:
            print("{0}\t{1}\t{2}".format(key, income_expense[key]["income"], income_expense[key]["expense"]))