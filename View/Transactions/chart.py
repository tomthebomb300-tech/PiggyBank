import customtkinter as ctk

from View.Transactions.selector import Selector
from View.Transactions.candle_stick_chart import Candle_stick_chart

class Chart(ctk.CTkFrame):
    def __init__(self, parent, controller, fg_color, corner_radius):
        super().__init__(parent, fg_color=fg_color, corner_radius=corner_radius)

        self.create_options(self)
        self.create_chart(self)

        self.charts = {
            "Candle_stick" : Candle_stick_chart(self, controller, fg_color = fg_color, corner_radius = corner_radius)
        }

        self.current_chart = None

        chart_selector = Selector(self, fg_color="transparent", items=list(self.charts.keys()), display_cmd=self.display_chart)
        chart_selector.pack(side = "top", anchor = "nw", padx = (20,0), pady = (20,0))


    def create_options(self, parent):
        pass

    def create_chart(self, parent):
        pass

    def display_chart(self, view):
        if self.current_chart:
            self.current_chart.pack_forget()

        self.current_chart = self.charts[view]
        self.current_chart.pack(side = "bottom", fill = "both", expand = True, pady = (0,15), padx = 15)
    