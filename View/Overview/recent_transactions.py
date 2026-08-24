import customtkinter as ctk

from PIL import Image

class Recent_transactions:
    def __init__(self, parent, controller):
        self.parent = parent
        self.controller = controller
        self.create_frame(parent)

    def create_frame(self, parent):
        transactions = self.controller.getRecentTransactions()
        recent_transactions_card = ctk.CTkFrame(parent, fg_color="#1d2228", corner_radius=5)
        recent_transactions_card.pack(side = "top", expand = True, fill = "both", padx = 10, pady = 10)

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
            imagePath = self.controller.getImagePath(trans)
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
    