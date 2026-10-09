import customtkinter as ctk
from tkinter import ttk

import datetime

class Order_stack(ctk.CTkFrame):
    def __init__(self, parent, fg_color, orders):
        super().__init__(parent, fg_color=fg_color)

        self.setup_table()
        self.update(orders)

    def setup_table(self):
        style = ttk.Style()
        style.theme_use("default")

        style.configure("Treeview",background="transparent",foreground="white",rowheight=30,fieldbackground="#1d2228")
        style.map("Treeview", background=[("selected", "#1f538d")])

        style.configure("Treeview.Heading",background="#343638",foreground="white",relief="flat",font=("Arial", 11, "bold"))
        style.map("Treeview.Heading", background=[("active", "#4a4a4a")])

        scrollbar = ctk.CTkScrollbar(self, orientation="vertical")
        scrollbar.pack(side="right", fill="y")

        columns = ("Date", "Quantity", "Price", "Device")
        
        self.tree = ttk.Treeview(self,columns=columns,show="headings",yscrollcommand=scrollbar.set,)
        self.tree.pack(fill="both", expand=True)

        scrollbar.configure(command=self.tree.yview)

        self.tree.heading("Date", text = "Date")
        self.tree.heading("Quantity", text = "Quantity")
        self.tree.heading("Price", text = "Price")
        self.tree.heading("Device", text = "Device")

        self.tree.column("Date", width = 80, anchor = "center")
        self.tree.column("Quantity", width = 80, anchor = "center")
        self.tree.column("Price", width = 80, anchor = "center")
        self.tree.column("Device", width = 80, anchor = "center")

    def update(self, orders):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for order in orders:
            self.tree.insert("", "end", values = (
                datetime.datetime.fromisoformat(order["filledAt"]).date(),
                round(order["quantity"],2),
                round(order["price"],2),
                order["initiatedFrom"]
            ))