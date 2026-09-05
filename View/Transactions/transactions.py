import customtkinter as ctk

from datetime import date
from View.Transactions.date_range_slider import Date_range_slider

class Transactions(ctk.CTkFrame):
    def __init__(self, parent, controller, fg_color, corner_radius):
        self.controller = controller
        super().__init__(parent, fg_color=fg_color, corner_radius=corner_radius)

        start_date = self.controller.getStartDate()
        last_date = self.controller.getLastDate()

        slider = Date_range_slider(parent=self,start_date=start_date,end_date=last_date,command=self.range_changed)
        slider.pack(fill="x", padx=20, pady=20)

    def range_changed(self, start, end):
        # print(start, end)
        pass