import customtkinter as ctk

from PIL import Image

class Authentication(ctk.CTkFrame):
    def __init__(self, parent, controller, fg_color, corner_radius):
        super().__init__(parent, fg_color = fg_color, corner_radius = corner_radius)
        self.controller = controller
        self.logging_in = True
        self.create_display(self)

    def create_display(self, parent):
        content = ctk.CTkFrame(parent, fg_color="#000000", corner_radius = 40)
        content.place(anchor = "center", relx = 0.5, rely = 0.5)

        img = Image.open("Images/Light/piggy_bank.png")
        image = ctk.CTkLabel(content, text = "", image = ctk.CTkImage(light_image=img, dark_image=img, size = (200,200)))
        image.pack(pady = (20,150))

        email_frame = ctk.CTkFrame(content,fg_color="#1D1D1D")
        email_frame.pack(padx = 50, pady = 25, fill = "x")
        img = Image.open("Images/Light/email.png")
        email_image = ctk.CTkLabel(email_frame, text = "", image = ctk.CTkImage(light_image=img, dark_image=img, size=(20,20)))
        email_image.pack(side = "left")
        self.email_entry = ctk.CTkEntry(email_frame,width=300,placeholder_text="Email", fg_color = "transparent", border_width=0)
        self.email_entry.pack(side = "left")

        password_frame = ctk.CTkFrame(content,fg_color="#1D1D1D")
        password_frame.pack(padx = 50, pady = 25, fill = "x")
        img = Image.open("Images/Light/password.png")
        password_image = ctk.CTkLabel(password_frame, text = "", image = ctk.CTkImage(light_image=img, dark_image=img, size=(20,20)))
        password_image.pack(side = "left")
        self.password_entry = ctk.CTkEntry(password_frame,width=300,placeholder_text="Password", fg_color = "transparent", border_width=0)
        self.password_entry.pack(side = "left")

        self.submit_button = ctk.CTkButton(content, text="Login", fg_color="#ffffff", text_color="#000000", command=self.submit)
        self.submit_button.pack()

        ctk.CTkLabel(content, text="OR", text_color="#ffffff").pack(pady = 30)

        img = Image.open("Images/Light/google.png")
        google_button = ctk.CTkButton(content, text = "", image = ctk.CTkImage(light_image=img, dark_image=img, size = (40,40)), fg_color="transparent", hover=False, command=self.google_login)
        google_button.pack(pady = (0,10))

        q_mode_frame = ctk.CTkFrame(content, fg_color="transparent")
        q_mode_frame.pack(pady = (0,10), padx = (40,0))
        self.question = ctk.CTkLabel(q_mode_frame, text="Don't have an account?", text_color="#ffffff")
        self.question.pack(side = "left")
        self.swap_mode_button = ctk.CTkButton(q_mode_frame, text="Sign Up", fg_color="transparent", text_color="#AF16C4", hover = "False", command=self.swap_submit_mode)
        self.swap_mode_button.pack(side = "right")

    def google_login(self):
        print("google")

    def swap_submit_mode(self):
        if(self.logging_in):
            self.swap_mode_button.configure(text = "Login")
            self.submit_button.configure(text = "Sign Up")
            self.question.configure(text = "Have an account?")
            self.logging_in = False
        else:
            self.swap_mode_button.configure(text = "Sign Up")
            self.submit_button.configure(text = "Login")
            self.question.configure(text = "Don't have an account?")
            self.logging_in = True


    def submit(self):
        if(self.logging_in):
            self.login()
        else:
            self.signup()


    def login(self):
        self.controller.login_user(self.email_entry.get(), self.password_entry.get())

    def signup(self):
        self.controller.signup_user(self.email_entry.get(), self.password_entry.get())
        