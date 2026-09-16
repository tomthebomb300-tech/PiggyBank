import customtkinter as ctk

from PIL import Image

class Content_selector(ctk.CTkFrame):
    def __init__(self, parent, fg_color, content_pages, display_content_page_cmd):
        super().__init__(parent, fg_color=fg_color)

        self.display_content_page_cmd = display_content_page_cmd

        self.buttons = {}
        for page in content_pages:
            self.buttons[page] = self.create_button("Images/Light/{0}.png".format(page), page)

        if(len(self.buttons) > 0):
            button_name = list(self.buttons.keys())[0]
            self.buttons[button_name].set_active(True)
            self.active_button = button_name
            self.display_content_page_cmd(button_name)


    def create_button(self, img_path, name):
        img = Image.open(img_path)
        button = Navigation_button(self, ctk.CTkImage(light_image=img, dark_image=img, size = (20,20)), lambda: self.clicked(name))
        button.pack(anchor = "w", fill = "x", pady = (0, 20), padx = (0,10), side = "left")
        return button

    def clicked(self, button_name):
        self.buttons[self.active_button].set_active(False)
        self.buttons[button_name].set_active(True)
        self.active_button = button_name
        self.display_content_page_cmd(button_name)


class Navigation_button(ctk.CTkButton):
    def __init__(self, parent, icon, command, active = False):
        super().__init__(
            parent, 
            image = icon, 
            command = command,
            anchor = "w",
            text = "",
            font=("Arial", 20),
            height=50,
            width = 50,
            corner_radius=18,
            fg_color="transparent",
            hover_color="#2a3846",
            border_width=0
            )

        self.active = active

    def set_active(self, active):
        self.active = active
        self.configure(fg_color="#0c0e11" if active else "transparent")
