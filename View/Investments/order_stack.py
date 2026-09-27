import customtkinter as ctk

class Order_stack(ctk.CTkFrame):
    def __init__(self, parent, fg_color, orders):
        super().__init__(parent, fg_color=fg_color)

        self.cards = []
        self.orders = orders
        self.visible_cards = 7
        self.start_index = 0

        for i in range(self.visible_cards):
            card = Order_card(self)
            card.place(x=0, y=i*50)
            self.cards.append(card)
        self.refresh_cards()
        self.bind_mousewheel()
        self.configure(width=500, height=220)

    def refresh_cards(self):
        for i, card in enumerate(self.cards):
            order_index = self.start_index + i
            if order_index < len(self.orders):
                card.update(self.orders[order_index])
                card.place_configure(y=i*50)
                card.place_configure(x=0)
            else:
                card.place_forget()
    
    def bind_mousewheel(self):
        self.bind("<MouseWheel>", self.on_scroll)
        for card in self.cards:
            card.bind("<MouseWheel>", self.on_scroll)

    def on_scroll(self, event):
        if event.delta < 0:         
            if self.start_index < len(self.orders) - self.visible_cards:
                self.start_index += 1
        else:               
            if self.start_index > 0:
                self.start_index -= 1
        self.refresh_cards()


class Order_card(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent,width=320,height=180,corner_radius=22,fg_color="#F5F5F2")
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
        self.price.configure(text=f"€{order['price']:.2f}")
