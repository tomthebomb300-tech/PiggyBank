import tkinter as tk

import customtkinter as ctk

from controller import Controller

controller = None

WIDTH = 1920
HEIGHT = 1080




def create_card(parent, title, value, subtitle):
    card = ctk.CTkFrame(parent,fg_color="#1d2228")
    card.pack(side="left",expand=True,fill="both",padx=10, pady=10)

    # Prevent the frame from resizing to its contents
    # card.pack_propagate(False)

    title_label = ctk.CTkLabel(card,text=title,font=("Arial", 20),text_color="white")
    title_label.pack(anchor="w",padx=20,pady=(20,0))

    value_label = ctk.CTkLabel(card,text=value,font=("Arial", 32),text_color="white")
    value_label.pack(anchor="w",padx=20,pady=(20,0))

    subtitle_label = ctk.CTkLabel(card,text=subtitle,font=("Arial", 16),text_color="#aaaaaa")
    subtitle_label.pack(anchor="w",padx=20,pady=(10,20))

    return value_label, subtitle_label



def main():
    controller = Controller()

    WINDOW = ctk.CTk();
    WINDOW.title("Finances")
    WINDOW.geometry("{0}x{1}".format(WIDTH, HEIGHT))

    dashboard = ctk.CTkFrame(WINDOW,fg_color="#30353b", corner_radius=15)
    dashboard.pack(fill="x",padx=40,pady=40)

    balance_value, balance_subtitle = create_card(dashboard,"Account","€{0}".format(controller.getBankBalance()),"")
    salary_value, salary_subtitle = create_card(dashboard,"Cash","€{0}".format(controller.getCashBalance()),"")
    savings_value, savings_subtitle = create_card(dashboard,"Investments","€Access trading212 API","Deposited: €{0}".format(controller.getInvestmentDeposits()))

    WINDOW.mainloop()


main()
    
