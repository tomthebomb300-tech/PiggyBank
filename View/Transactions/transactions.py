import customtkinter as ctk

from View.Transactions.search import Search
from View.Transactions.candle_stick_chart import Candle_stick_chart
from View.Transactions.selector import Selector

class Transactions(ctk.CTkFrame):
    def __init__(self, parent, controller, fg_color, corner_radius):
        super().__init__(parent, fg_color=fg_color, corner_radius=corner_radius)
        self.controller = controller

        self.views = {
            "Candle_stick": Candle_stick_chart(self, controller, fg_color = fg_color, corner_radius = corner_radius),
            "Search": Search(self, controller, fg_color=fg_color, corner_radius=corner_radius)
        }

        self.current_view = None

        view_selector = Selector(self, fg_color="transparent", items=list(self.views.keys()), display_cmd=self.display_view)
        view_selector.pack(side = "top", anchor = "nw", padx = (20,0), pady = (20,0))

    def display_view(self, view):
        if self.current_view:
            self.current_view.pack_forget()

        self.current_view = self.views[view]
        self.current_view.pack(side = "bottom", fill = "both", expand = True, pady = (0,15), padx = 15)
