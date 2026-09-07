import customtkinter as ctk

from PIL import Image

class Category_selector(ctk.CTkFrame):
    def __init__(self, parent, categories, corner_radius):
        super().__init__(parent, fg_color="#1d2228", corner_radius=corner_radius)

        self.selected_frame = ctk.CTkFrame(self, fg_color="#306901", corner_radius=0)
        self.selected_frame.pack(fill = "x", side = "right", anchor = "n", padx = 20, pady = 20)
        label = ctk.CTkLabel(self.selected_frame, text = "Selected", font = ("Arial", 20), text_color = "white")
        label.pack(padx=50)

        self.unselected_frame = ctk.CTkFrame(self, fg_color = "#680404", corner_radius=0)
        self.unselected_frame.pack(fill = "x", side = "left", anchor = "n", padx = 20, pady = 20)
        label = ctk.CTkLabel(self.unselected_frame, text = "Un-Selected", font = ("Arial", 20), text_color = "white", corner_radius=0)
        label.pack(padx = 50)

        self.selected = {}
        self.unselected = {}
        for c in categories:
            self.selected[c] = self.__create_button(self.selected_frame, "Images/Light/settings.png", c, self.unselect, "transparent")

        

    def __create_button(self, parent, img_path, name, command, colour):
        img = Image.open(img_path)
        button = ctk.CTkButton(parent, text = name, image=ctk.CTkImage(light_image=img, dark_image=img, size = (16,16)), command=lambda: command(name), fg_color=colour, corner_radius=0)
        button.pack(anchor = "w", fill = "x")
        return button

    def select(self, category):
        self.unselected[category].pack_forget()
        del self.unselected[category]
        self.selected[category] = self.__create_button(self.selected_frame, "Images/Light/settings.png", category, self.unselect, "transparent")

    def unselect(self, category):
        self.selected[category].pack_forget()
        del self.selected[category]
        self.unselected[category] = self.__create_button(self.unselected_frame, "Images/Light/settings.png", category, self.select, "transparent")

    def get_selected(self):
        return list(self.selected.keys())