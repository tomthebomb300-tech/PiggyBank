import customtkinter as ctk

from View.Transactions.date_range_slider import Date_range_slider
from View.Transactions.category_selector import Category_selector
from View.Transactions.pies import Pies
from View.Transactions.table import Table
from View.Transactions.chart import Chart
from View.Transactions.selector import Selector

class Search(ctk.CTkFrame):
    def __init__(self, parent, controller, fg_color, corner_radius):
        super().__init__(parent, fg_color=fg_color, corner_radius=corner_radius)
        self.controller = controller

        self.start_date = self.controller.getStartDate()
        self.last_date = self.controller.getLastDate()

        slider_fetch_frame = ctk.CTkFrame(self, fg_color="transparent")
        slider_fetch_frame.pack(fill = "x", padx = 20, pady = (0,0))
        slider_fetch_frame.grid_columnconfigure(0, weight=1)
        slider_fetch_frame.grid_columnconfigure(1, weight=0)

        slider = Date_range_slider(parent=slider_fetch_frame,start_date=self.start_date,end_date=self.last_date,command=self.range_changed)
        slider.grid(row = 0, column = 0, sticky = "ew", padx=(0,20), pady=0)

        fetch_button = ctk.CTkButton(slider_fetch_frame, text="Fetch", command=self.fetch)
        fetch_button.grid(row = 0, column = 1, sticky = "ns", padx = 20, pady = 0)


        self.category_selector = Category_selector(parent=self, categories=self.controller.getCategories(), fg_color="#1d2228", corner_radius=40)
        self.category_selector.pack(side = "left", fill = "y", padx = 20, pady = 20)

        content_frame = ctk.CTkFrame(self, fg_color="#1d2228", corner_radius = 40)
        content_frame.pack(padx = 20, pady = 20, fill = "both", expand = True)

        self.content_pages = {
            "Pies": Pies(content_frame, fg_color="transparent", corner_radius=40),
            "Table": Table(content_frame, fg_color="transparent", corner_radius=40),
            "Chart": Chart(content_frame, controller, fg_color="transparent", corner_radius=40)
        }
        self.current_content_page = None

        content_selector = Selector(content_frame, "transparent", list(self.content_pages.keys()), self.display_content_page)
        content_selector.pack(side = "top", anchor = "w", padx = 20, pady = (20,0))

        self.fetch()
        

    def range_changed(self, start, end):
        self.start_date = start
        self.last_date = end

    def fetch(self):
        income = self.controller.getIncome(self.category_selector.get_selected(), self.start_date, self.last_date)
        expense = self.controller.getExpense(self.category_selector.get_selected(), self.start_date, self.last_date)
        for key in expense: expense[key] *= -1
        self.content_pages["Pies"].update(income, expense)
        self.content_pages["Table"].update_transactions(
            self.controller.getTransactions(self.category_selector.get_selected(), 
                                            self.start_date, 
                                            self.last_date)
                                            )

    def display_content_page(self, page_name):
        if self.current_content_page:
            self.current_content_page.pack_forget()

        self.current_content_page = self.content_pages[page_name]
        self.current_content_page.pack(side = "bottom", fill = "both", expand = True, padx=20, pady=(0,20))

    