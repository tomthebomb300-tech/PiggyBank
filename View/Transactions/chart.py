import customtkinter as ctk

from View.Transactions.selector import Selector
from View.Transactions.candle_stick_chart import Candle_stick_chart

class Chart(ctk.CTkFrame):
    def __init__(self, parent, controller, fg_color, corner_radius):
        super().__init__(parent, fg_color=fg_color, corner_radius=corner_radius)

        self.charts = {
            "Candle_stick" : Candle_stick_chart(self, controller, fg_color = fg_color, corner_radius = corner_radius)
        }

        self.current_chart = None

        chart_selector = Selector(self, fg_color="transparent", items=list(self.charts.keys()), display_cmd=self.display_chart)
        chart_selector.pack(side = "top", anchor = "nw", padx = (20,0), pady = (20,0))

    def update(self, transactions):
        categories = set([trans["Category"] for trans in transactions])

        for chart in self.charts:
            self.charts[chart].update(categories)

    def display_chart(self, chart):
        if self.current_chart:
            self.current_chart.pack_forget()

        self.current_chart = self.charts[chart]
        self.current_chart.pack(side = "bottom", fill = "both", expand = True, pady = (0,15), padx = 15)
    