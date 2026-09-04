import customtkinter as ctk

class Summary_cards(ctk.CTkFrame):
    def __init__(self, parent, controller, fg_color, corner_radius):
        super().__init__(parent, fg_color=fg_color, corner_radius=corner_radius)
        self.controller = controller

        self.create_card("Account","€{0}".format(self.controller.getBankBalance()),"")
        self.create_card("Cash","€{0}".format(self.controller.getCashBalance()),"")
        self.create_card("Investments Value","€{0}".format(self.controller.getPortfolioValue()),"Deposited: €{0}".format(self.controller.getInvestmentDeposits()))

    def create_card(self, title, value, subtitle):
        card = ctk.CTkFrame(self,fg_color="#1d2228", corner_radius=40)
        card.pack(side="left",expand=True,fill="both",padx=10, pady=10)

        title_label = ctk.CTkLabel(card,text=title,font=("Arial", 20),text_color="white")
        title_label.pack(anchor="w",padx=20,pady=(20,0))

        value_label = ctk.CTkLabel(card,text=value,font=("Arial", 32),text_color="white")
        value_label.pack(anchor="w",padx=20,pady=(20,0))

        subtitle_label = ctk.CTkLabel(card,text=subtitle,font=("Arial", 16),text_color="#aaaaaa")
        subtitle_label.pack(anchor="w",padx=20,pady=(10,20))