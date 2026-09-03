import customtkinter as ctk

from View.Overview.summary_cards import Summary_cards
from View.Overview.recent_transactions import Recent_transactions
from View.Overview.month_expenses import Month_expenses
from View.Overview.balances_chart import Balances_chart

class Dashboard:
    def __init__(self, window_frame, controller):
        self.window_frame = window_frame
        self.controller = controller

        self.create_frame(self.window_frame)

    def create_frame(self, parent):
        frame = ctk.CTkFrame(parent, fg_color = "#30353b", corner_radius=40)
        frame.pack(fill = "both", padx=40, pady=40)
        self.create_dashboard(frame)

    def create_right_side(self, parent):
        frame = ctk.CTkFrame(parent, fg_color = "#30353b", corner_radius=40)
        frame.pack(side = "right", padx=(5,20), pady=20)

        Recent_transactions(frame, self.controller)
        Month_expenses(frame, self.controller)

    def create_left_side(self, parent):
        frame = ctk.CTkFrame(parent, fg_color = "#30353b", corner_radius=40)
        frame.pack(fill = "both", expand = True, side = "left", padx = (20,5), pady = 20)
        
        Summary_cards(frame, self.controller)
        Balances_chart(frame, self.controller)
        

    def create_dashboard(self, parent):
        self.create_left_side(parent)
        self.create_right_side(parent)