import customtkinter as ctk

from PIL import Image

class Recent_transactions(ctk.CTkFrame):
    def __init__(self, parent, controller, fg_color, corner_radius):
        super().__init__(parent, fg_color=fg_color, corner_radius=corner_radius)

        self.controller = controller
        self.create_frame()

    def create_frame(self):
        transactions = self.controller.getRecentTransactions()

        label = ctk.CTkLabel(self, text = "Recent Transactions", font = ("Arial", 20), text_color = "white")
        label.pack(anchor = "w", pady = (20,10), padx = 40)

        border_line = ctk.CTkFrame(self, height=2, fg_color="#353b44")
        border_line.pack(fill = "x", padx = 40, pady = (5, 10))

        scrollable = ctk.CTkScrollableFrame(self, fg_color="#1d2228", corner_radius=40)
        scrollable.pack(side = "left", expand = True, fill = "both", padx = 10, pady = (0,15))

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
    