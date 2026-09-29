import customtkinter as ctk

class Order_stack(ctk.CTkFrame):
    def __init__(self, parent, fg_color, orders):
        super().__init__(parent, fg_color=fg_color)
        self.card_height = 180
        self.card_width = 320
        self.configure(width=self.card_width)

        self.cards = []
        self.orders = orders
        self.visible_cards = 5
        self.current_index = 18

        for i in range(self.visible_cards):
            self.cards.append(Order_card(self, self.card_width, self.card_height))

        self.update_cards()
        self.bind_mousewheel()

    def update_cards(self):
        for i, card in enumerate(self.cards):
            order_index = self.current_index + i
            if order_index < len(self.orders):
                card.update(self.orders[order_index])
                card.place_configure(anchor = "center", relx = 0.5, rely = 0.5)

                next_card = self.cards[i-1]
                next_card.update(self.orders[self.current_index + i-1])
                next_card.place_configure(anchor = "center", relx = 0.5, rely = 0.6)
            else:
                card.place_forget()
    
    def bind_mousewheel(self):
        self.bind("<MouseWheel>", self.on_scroll)
        for card in self.cards:
            card.bind("<MouseWheel>", self.on_scroll)

    def on_scroll(self, event):
        if(event.delta < 0):
            if(self.current_index > 0):
                self.current_index -= 1
        else:
            if(self.current_index < len(self.orders)-1):
                self.current_index += 1
        self.update_cards()





class Order_card(ctk.CTkFrame):
    def __init__(self, parent, width, height):
        super().__init__(parent,width,height,corner_radius=22,fg_color="#F5F5F2")
        self.pack_propagate(False)

        self.asset = ctk.CTkLabel(self,font=("Arial", 20, "bold"),text_color="black")
        self.asset.place(x=20, y=20)

        self.side = ctk.CTkLabel(self,font=("Arial", 14),text_color="#05c234")
        self.side.place(x=20, y=50)

        self.filledValue = ctk.CTkLabel(self,font=("Arial", 30, "bold"),text_color="black")
        self.filledValue.place(x=20, y=105)

        self.quantity = ctk.CTkLabel(self,text_color="gray20")
        self.quantity.place(x=20, y=150)

        self.price = ctk.CTkLabel(self,text_color="gray20")
        self.price.place(x=190, y=150)

    def update(self, order):
        self.asset.configure(text=order["instrument"]["name"])
        self.side.configure(text=order["side"])
        self.filledValue.configure(text=f"€{order['filledValue']:.2f}")
        self.quantity.configure(text=f"{order['quantity']:.4f}")
        self.price.configure(text=f"£{order['price']:.2f}")
