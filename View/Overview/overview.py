import customtkinter as ctk

from View.Overview.summary_cards import Summary_cards
from View.Overview.recent_transactions import Recent_transactions
from View.Overview.month_expenses import Month_expenses
from View.Overview.balances_chart import Balances_chart

class Overview(ctk.CTkFrame):
    def __init__(self, parent, controller, fg_color, corner_radius):
        super().__init__(parent, fg_color=fg_color, corner_radius=corner_radius)
        
        self.controller = controller
        self.create_left_side(self)
        self.create_right_side(self)

    def create_right_side(self, parent):
        frame = ctk.CTkFrame(parent, fg_color = "#30353b", corner_radius=40)
        frame.pack(side = "right", padx=(5,20), pady=20)

        recent_transactions = Recent_transactions(frame, self.controller, fg_color="#1d2228", corner_radius=40)
        recent_transactions.pack(side = "top", expand = True, fill = "both", padx = 10, pady = 10)

        month_expenses = Month_expenses(frame, self.controller, fg_color="#1d2228", corner_radius=40)
        month_expenses.pack(side = "bottom", padx = 10, pady = 10)

    def create_left_side(self, parent):
        frame = ctk.CTkFrame(parent, fg_color = "#30353b", corner_radius=40)
        frame.pack(fill = "both", expand = True, side = "left", padx = (20,5), pady = 20)
        
        summary_cards = Summary_cards(frame, self.controller, fg_color="#30353b", corner_radius=40)
        summary_cards.pack(fill = "x")

        balances_chart = Balances_chart(frame, self.controller, fg_color="#1d2228", corner_radius=40)
        balances_chart.pack(side = "bottom", fill = "both", expand = True, padx = 10, pady = 10)