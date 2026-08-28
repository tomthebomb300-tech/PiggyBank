import customtkinter as ctk

from View.Overview.summary_cards import Summary_cards
from View.Overview.recent_transactions import Recent_transactions
from View.Overview.month_expenses import Month_expenses
from View.Overview.balances_chart import Balances_chart

class Dashboard:
    def __init__(self, window, controller):
        self.window = window
        self.controller = controller

        self.create_frame(self.window)

    def create_frame(self, parent):
        frame = ctk.CTkFrame(parent,fg_color="#30353b")
        frame.pack(fill = "both", padx=40, pady=40)
        self.create_dashboard(frame)

    def create_right_side(self, parent):
        frame = ctk.CTkFrame(parent, fg_color = "#30353b")
        frame.pack(side = "right")

        Recent_transactions(frame, self.controller)
        Month_expenses(frame, self.controller)

    def create_left_side(self, parent):
        frame = ctk.CTkFrame(parent, fg_color="#30353b")
        frame.pack(fill = "both", expand = True, side = "left")
        
        Summary_cards(frame, self.controller)
        Balances_chart(frame, self.controller)
        

    def create_dashboard(self, parent):
        self.create_left_side(parent)
        self.create_right_side(parent)