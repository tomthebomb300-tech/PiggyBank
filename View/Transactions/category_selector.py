import customtkinter as ctk

from PIL import Image

class Category_selector(ctk.CTkFrame):
    def __init__(self, parent, categories):
        super().__init__(parent, fg_color="transparent")

        self.selected_frame = ctk.CTkFrame(self, fg_color="#000000")
        self.selected_frame.pack()

        self.unselected_frame = ctk.CTkFrame(self, fg_color = "#4D1515")
        self.unselected_frame.pack()

        self.selected = {}
        self.unselected = {}
        for c in categories:
            self.unselected[c] = self.__create_button(self.unselected_frame, "Images/Light/settings.png", c, self.select, "#B10707")

        

    def __create_button(self, parent, img_path, name, command, colour):
        img = Image.open(img_path)
        button = ctk.CTkButton(parent, text = name, image=ctk.CTkImage(light_image=img, dark_image=img, size = (16,16)), command=lambda: command(name), fg_color=colour)
        button.pack(anchor = "w", fill = "x")
        return button

    def select(self, category):
        self.unselected[category].pack_forget()
        del self.unselected[category]
        self.selected[category] = self.__create_button(self.selected_frame, "Images/Light/settings.png", category, self.unselect, "#4E5702")

    def unselect(self, category):
        self.selected[category].pack_forget()
        del self.selected[category]
        self.unselected[category] = self.__create_button(self.unselected_frame, "Images/Light/settings.png", category, self.select, "#B10707")

    def draw_selected(self):
        pass