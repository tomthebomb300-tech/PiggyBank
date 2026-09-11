import customtkinter as ctk

from View.Overview.overview import Overview
from View.Transactions.transactions import Transactions
from View.sidebar import Sidebar


class Window(ctk.CTk):
    def __init__(self, name, height, width, controller):
        super().__init__()
        self.controller = controller

        self.title(name)
        self.geometry("{0}x{1}".format(width, height))

        self.window_frame = ctk.CTkFrame(self, fg_color = "#191c1f", corner_radius=0)
        self.window_frame.pack(fill = "both", expand = True)

        sidebar = Sidebar(self.window_frame, self.controller, fg_color = "#191c1f")
        sidebar.pack(side = "left", anchor = "n", pady = (70,0), padx = (0,10))

        self.content = ctk.CTkFrame(self.window_frame, fg_color="#191c1f")
        self.content.pack(fill = "both", expand = True)

        self.pages = {
            "overview": Overview(self.content, self.controller, fg_color ="#30353b", corner_radius = 40),
            "transactions": Transactions(self.content, self.controller, fg_color = "#30353b", corner_radius=40)
        }

        self.current_page = None
        self.display_page("transactions")

    def run(self):
        self.mainloop()

    def display_page(self, page_name):
        if self.current_page:
            self.current_page.pack_forget()

        self.current_page = self.pages[page_name]
        self.current_page.pack(fill = "both", expand = True, padx=40, pady=40)