import customtkinter as ctk
import pyrebase

class Authentication(ctk.CTkFrame):
    def __init__(self, parent, controller, fg_color, corner_radius):
        super().__init__(parent, fg_color = fg_color, corner_radius = corner_radius)
        self.controller = controller

        firebaseConfig = {
            "apiKey": "AIzaSyDPW7Yqg_FypzAqnZ_-j810aSTm_TxaiC0",
            "authDomain": "piggybank-71e18.firebaseapp.com",
            "projectId": "piggybank-71e18",
            "storageBucket": "piggybank-71e18.firebasestorage.app",
            "messagingSenderId": "762660149537",
            "appId": "1:762660149537:web:84d8e3aaa378f21aff4660",
            "measurementId": "G-ETLKHQ3VVW",
            "databaseURL": ""
        }
        firebase = pyrebase.initialize_app(firebaseConfig)
        self.auth=firebase.auth()

        self.create_display(self)

    def create_display(self, parent):
        content = ctk.CTkFrame(parent, fg_color="#ffffff", corner_radius = 40)
        content.place(anchor = "center", relx = 0.5, rely = 0.5)

        title = ctk.CTkLabel(content, text="Welcome login", font=("Arial", 20), text_color="black")
        title.pack(padx = 50, pady = 50)

        self.email_entry = ctk.CTkEntry(content,width=300,placeholder_text="Email")
        self.email_entry.pack(padx = 50, pady = 50)

        self.password_entry = ctk.CTkEntry(content,width=300,placeholder_text="Password",show="*")
        self.password_entry.pack(padx = 50, pady = 50)

        signup = ctk.CTkButton(content, text="Sign Up", width = 50, height = 50, corner_radius=18, fg_color="crimson", command=self.signup)
        signup.pack()
        login = ctk.CTkButton(content, text="Login", width = 50, height = 50, corner_radius=18, fg_color="crimson", command=self.login)
        login.pack()

    def login(self):
        print("Login")
        print(self.email_entry.get())
        print(self.password_entry.get())
        try:
            login = self.auth.sign_in_with_email_and_password(self.email_entry.get(), self.password_entry.get())
            print("Success")
        except:
            print("Invalid Email or Password")

    def signup(self):
        print("Sign up")
        print(self.email_entry.get())
        print(self.password_entry.get())
        try:
            user = self.auth.create_user_with_email_and_password(self.email_entry.get(), self.password_entry.get())
            print("Success")
        except:
            print("Email already exists")