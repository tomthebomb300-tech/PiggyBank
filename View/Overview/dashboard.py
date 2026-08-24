import customtkinter as ctk

from View.Overview.summary_cards import Summary_cards
from View.Overview.recent_transactions import Recent_transactions
from View.Overview.month_expenses import Month_expenses

class Dashboard:
    def __init__(self, window, controller):
        self.window = window
        self.controller = controller

        self.create_frame(self.window)
        self.create_dashboard(self.frame)

    def create_frame(self, parent):
        self.frame = ctk.CTkFrame(parent,fg_color="#30353b", corner_radius=15)
        self.frame.pack(fill="x",padx=40,pady=40)

    def create_right_side(self, parent):
        Recent_transactions(parent, self.controller)
        Month_expenses(parent, self.controller)

    def create_left_side(self, parent):
        Summary_cards(parent, self.controller)

    def create_dashboard(self, parent):
        self.create_left_side(parent)
        self.create_right_side(parent)