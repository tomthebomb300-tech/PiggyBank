import customtkinter as ctk

class Summary_cards:
    def __init__(self, parent, controller):
        self.create_card(parent,"Account","€{0}".format(controller.getBankBalance()),"")
        self.create_card(parent,"Cash","€{0}".format(controller.getCashBalance()),"")
        self.create_card(parent,"Investments","€Access trading212 API","Deposited: €{0}".format(controller.getInvestmentDeposits()))

    def create_card(self, parent, title, value, subtitle):
        card = ctk.CTkFrame(parent,fg_color="#1d2228")
        card.pack(side="left",expand=True,fill="both",padx=10, pady=10)

        title_label = ctk.CTkLabel(card,text=title,font=("Arial", 20),text_color="white")
        title_label.pack(anchor="w",padx=20,pady=(20,0))

        value_label = ctk.CTkLabel(card,text=value,font=("Arial", 32),text_color="white")
        value_label.pack(anchor="w",padx=20,pady=(20,0))

        subtitle_label = ctk.CTkLabel(card,text=subtitle,font=("Arial", 16),text_color="#aaaaaa")
        subtitle_label.pack(anchor="w",padx=20,pady=(10,20))