import customtkinter as ctk

from PIL import Image

class Category_selector(ctk.CTkFrame):
    def __init__(self, parent, categories, fg_color, corner_radius):
        super().__init__(parent, fg_color=fg_color, corner_radius=corner_radius)

        frame = ctk.CTkFrame(self, fg_color="transparent")
        frame.pack(side = "top", padx = 20, pady = (40,0))
        select_all_button = ctk.CTkButton(frame, text="", width = 50, height = 50, corner_radius=18, fg_color="green", command=self.select_all)
        select_all_button.pack(side = "left", padx = (0,10))

        unselect_all_button = ctk.CTkButton(frame, text="", width = 50, height = 50, corner_radius=18, fg_color="crimson", command=self.unselect_all)
        unselect_all_button.pack(side = "right", padx = (10,0))

        button_frame = ctk.CTkScrollableFrame(self, fg_color = "transparent")
        button_frame.pack(padx = 20, pady = 20, expand = True, fill = "y", side = "bottom")

        self.selected = []
        self.unselected = []
        self.buttons = {}
        for c in categories:
            self.buttons[c] = self.__create_button(button_frame, "Images/Light/settings.png", c, self.unselect, "green")
            self.selected.append(c)


    def select_all(self):
        while(len(self.unselected) > 0):
            self.select(self.unselected[0])

    def unselect_all(self):
        while(len(self.selected) > 0):
            self.unselect(self.selected[0])

    def __create_button(self, parent, img_path, name, command, colour):
        img = Image.open(img_path)
        button = ctk.CTkButton(parent, text = name, font=("Arial", 15), image=ctk.CTkImage(light_image=img, dark_image=img, size = (16,16)), command=lambda: command(name), fg_color=colour, corner_radius=10)
        button.pack(fill = "x", padx = 0, pady = (0,5))
        return button

    def select(self, category):
        self.buttons[category].configure(fg_color = "green", command = lambda: self.unselect(category))
        self.unselected.remove(category)
        self.selected.append(category)

    def unselect(self, category):
        self.buttons[category].configure(fg_color = "crimson", command = lambda: self.select(category))
        self.selected.remove(category)
        self.unselected.append(category)

    def get_selected(self):
        return self.selected