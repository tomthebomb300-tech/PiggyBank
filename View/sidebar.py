import customtkinter as ctk

from PIL import Image

class Sidebar(ctk.CTkFrame):
    def __init__(self, parent, controller, fg_color):
        super().__init__(parent, fg_color=fg_color)
        self.controller = controller
        self.buttons = {}

        self.__create_buttons()


    def __create_buttons(self):
        name = "Dashboard"
        self.buttons[name] = self.__create_button("Images/Light/dashboard.png", name, self.display_dashboard)
        name = "Transactions"
        self.buttons[name] = self.__create_button("Images/Light/transactions.png", name, self.display_transactions)
        name = "Investments"
        self.buttons[name] = self.__create_button("Images/Light/investments.png", name, self.dislpay_investments)
        name = "Settings"
        self.buttons[name] = self.__create_button("Images/Light/settings.png", name, self.display_settings)

    def __create_button(self, img_path, name, command):
        img = Image.open(img_path)
        button = Navigation_button(self, name, ctk.CTkImage(light_image=img, dark_image=img, size = (16,16)), command)
        button.pack(anchor = "w", fill = "x", pady = (0, 20))
        return button

    def display_dashboard(self):
        print("Dashboard")

    def display_transactions(self):
        print("Transactions")

    def dislpay_investments(self):
        print("Investments")

    def display_settings(self):
        print("Settings")



class Navigation_button(ctk.CTkButton):
    def __init__(self, parent, text, icon, command, active = False):
        super().__init__(
            parent, 
            text = text, 
            image = icon, 
            command = command,
            anchor = "w",
            font=("Arial", 20),
            height=34,
            corner_radius=18,
            fg_color="transparent",
            hover_color="#7C5EF0",
            text_color="white",
            border_width=0
            )

        self.active = active

    def set_active(self, active):
        self.active = active

        self.configure(
            fg_color="#8B6EF8" if active else "transparent",
            hover_color="#7C5EF0" if active else "#3A3A3A"
        )
