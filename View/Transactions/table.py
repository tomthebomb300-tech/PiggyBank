import customtkinter as ctk
from tkinter import ttk

class Table(ctk.CTkFrame):
    def __init__(self, parent, fg_color, corner_radius):
        super().__init__(parent, fg_color=fg_color, corner_radius=corner_radius)

        self.setup_table()

    def setup_table(self):
        style = ttk.Style()
        style.theme_use("default")

        style.configure("Treeview",background="transparent",foreground="white",rowheight=30,fieldbackground="#1d2228")
        style.map("Treeview", background=[("selected", "#1f538d")])

        style.configure("Treeview.Heading",background="#343638",foreground="white",relief="flat",font=("Arial", 11, "bold"))
        style.map("Treeview.Heading", background=[("active", "#4a4a4a")])

        scrollbar = ctk.CTkScrollbar(self, orientation="vertical")
        scrollbar.pack(side="right", fill="y")

        columns = ("Date", "Amount", "Payment Method", "Shop/Person", "Category")

        self.tree = ttk.Treeview(self,columns=columns,show="headings",yscrollcommand=scrollbar.set,)
        self.tree.pack(fill="both", expand=True)

        scrollbar.configure(command=self.tree.yview)    #Link scrollbar  to treeview

        self.tree.heading("Date", text="Date")
        self.tree.heading("Amount", text="Amount")
        self.tree.heading("Payment Method", text="Payment Method")
        self.tree.heading("Shop/Person", text="Shop/Person")
        self.tree.heading("Category", text="Category")

        self.tree.column("Date", width=80, anchor="center")
        self.tree.column("Amount", width=120, anchor="center")
        self.tree.column("Payment Method", width=100, anchor="center")
        self.tree.column("Shop/Person", width=280, anchor="center")
        self.tree.column("Category", width=100, anchor="center")

    def update_transactions(self, transactions):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for trans in transactions:
            self.tree.insert("", "end", values=(
                trans["Date"].date(),
                trans["Amount"],
                trans["Payment Method"],
                trans["Shop/Person"],
                trans["Category"]
            ))
