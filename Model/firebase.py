import pyrebase
import os
import requests

from google_auth_oauthlib.flow import InstalledAppFlow

class Firebase:
    def __init__(self):
        firebaseConfig = {
            "apiKey": os.getenv("apiKey"),
            "authDomain": os.getenv("authDomain"),
            "projectId": os.getenv("projectId"),
            "storageBucket": os.getenv("storageBucket"),
            "messagingSenderId": os.getenv("messagingSenderId"),
            "appId": os.getenv("appId"),
            "measurementId": os.getenv("measurementId"),
            "databaseURL": os.getenv("databaseURL") 
        }
        firebase = pyrebase.initialize_app(firebaseConfig)
        self.auth=firebase.auth()

    def login_user(self, email, password):
        try:
            login = self.auth.sign_in_with_email_and_password(email, password)
            return True
        except:
            print("Invalid Email or Password")
            return False

    def signup_user(self, email, password):
        try:
            user = self.auth.create_user_with_email_and_password(email, password)
            return True
        except:
            print("Email already exists")
            return False