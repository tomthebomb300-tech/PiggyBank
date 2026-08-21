import customtkinter as ctk

from PIL import Image
from controller import Controller

controller = Controller()

WIDTH = 1920
HEIGHT = 1080




def create_card(parent, title, value, subtitle):
    card = ctk.CTkFrame(parent,fg_color="#1d2228")
    card.pack(side="left",expand=True,fill="both",padx=10, pady=10)

    title_label = ctk.CTkLabel(card,text=title,font=("Arial", 20),text_color="white")
    title_label.pack(anchor="w",padx=20,pady=(20,0))

    value_label = ctk.CTkLabel(card,text=value,font=("Arial", 32),text_color="white")
    value_label.pack(anchor="w",padx=20,pady=(20,0))

    subtitle_label = ctk.CTkLabel(card,text=subtitle,font=("Arial", 16),text_color="#aaaaaa")
    subtitle_label.pack(anchor="w",padx=20,pady=(10,20))

    return value_label, subtitle_label


def create_left_side(parent):
    balance_value, balance_subtitle = create_card(parent,"Account","€{0}".format(controller.getBankBalance()),"")
    salary_value, salary_subtitle = create_card(parent,"Cash","€{0}".format(controller.getCashBalance()),"")
    savings_value, savings_subtitle = create_card(parent,"Investments","€Access trading212 API","Deposited: €{0}".format(controller.getInvestmentDeposits()))


def getImagePath(transaction):
    image = "Images/Light/{0}.png"
    c = transaction["Category"]
    if(c == "BOI Fees"):
        return image.format("BOI")
    if(c == "Car"):
        return image.format("Car")
    if(c == "Clothes"):
        return image.format("Clothes")
    if(c == "Entertainment"):
        return image.format("Entertainment")
    if(c=="Food" or c=="Impulsive Food" or c=="Food Non-Personal"):
        if(transaction["Shop/Person"] == "Lidl"):
            return image.format("Lidl")
        if(transaction["Shop/Person"] == "Tesco"):
            return image.format("Tesco")
        return image.format("Food")
    if(c == "Household"):
        return image.format("Household")
    if(c == "Income"):
        return image.format("Income")
    if(c == "Investing"):
        return image.format("Investing")
    if(c == "Trading"):
        return image.format("Trading")
    if(c=="Mumsie" or c=="Dadsie" or c=="Michael" or c=="Sheila" or c=="Denis" or c=="Alexia"):
        return image.format("People")
    if(c == "Personal Development"):
        return image.format("Personal Development")
    if(c == "Personal"):
        return image.format("Personal")
    if(c == "Rent"):
        return image.format("Rent")
    if(c == "Transport"):
        return image.format("Transport")

    return "Images/Light/Null.png"

def create_recent_transactions(parent, transactions):
    recent_transactions_card = ctk.CTkFrame(parent, fg_color="#1d2228", corner_radius=5)
    recent_transactions_card.pack(side = "left", expand = True, fill = "both", padx = 10, pady = 10)

    label = ctk.CTkLabel(recent_transactions_card, text = "Recent Transactions", font = ("Arial", 20), text_color = "white")
    label.pack(anchor = "w", pady = (20,10), padx = 20)

    border_line = ctk.CTkFrame(recent_transactions_card, height=2, fg_color="#353b44")
    border_line.pack(fill = "x", padx = 20, pady = (5, 10))

    scrollable = ctk.CTkScrollableFrame(recent_transactions_card, fg_color="#1d2228", corner_radius=5)
    scrollable.pack(side = "left", expand = True, fill = "both", padx = 10, pady = 10)

    for key in transactions:
        transaction_card = ctk.CTkFrame(scrollable, fg_color="#1d2228")
        transaction_card.pack(side = "top", expand = True, fill = "both", padx = 20, pady = (0,10))

        trans = transactions[key]
        entry = "- €{0}".format(trans["Amount"]*-1)
        txt_colour = "#CC1100"

        if(trans["Amount"] > 0):
            entry = "€{0}".format(trans["Amount"])
            txt_colour = "#32CD32"


        #left = image
        imagePath = getImagePath(trans)
        icon = ctk.CTkImage(light_image=Image.open(imagePath), dark_image=Image.open(imagePath), size=(40,40))
        label = ctk.CTkLabel(transaction_card, image=icon, text="")
        label.pack(side = "left", padx = 20)

        #middle = transaction name + date
        middle_frame = ctk.CTkFrame(transaction_card, fg_color = "#1d2228")
        middle_frame.pack(side="left")

        label = ctk.CTkLabel(middle_frame, text = trans["Shop/Person"], font = ("Arial", 16), text_color = "white")
        label.pack(anchor = "w")
        label = ctk.CTkLabel(middle_frame, text = trans["Date"].date(), font = ("Arial", 12), text_color = "#49515c")
        label.pack(anchor = "w")

        #right = amount
        right_frame = ctk.CTkFrame(transaction_card, fg_color="#1d2228")
        right_frame.pack(side = "right", padx = 10)

        amount = ctk.CTkLabel(right_frame, text = entry, font = ("Arial", 16, "bold"), text_color = txt_colour)
        amount.pack(anchor = "w")


def create_right_side(parent):
    create_recent_transactions(parent, controller.getRecentTransactions())


def create_dashboard(parent):
    dashboard = ctk.CTkFrame(parent,fg_color="#30353b", corner_radius=15)
    dashboard.pack(fill="x",padx=40,pady=40)
    return dashboard



def main():
    WINDOW = ctk.CTk();
    WINDOW.title("Finances")
    WINDOW.geometry("{0}x{1}".format(WIDTH, HEIGHT))

    dashboard = create_dashboard(WINDOW)

    create_left_side(dashboard)
    create_right_side(dashboard)

    WINDOW.mainloop()


main()
    
