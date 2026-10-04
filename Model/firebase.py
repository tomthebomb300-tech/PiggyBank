import pyrebase
import os
import requests

from google_auth_oauthlib.flow import InstalledAppFlow

class Firebase:
    def __init__(self):
        self.api_key = os.getenv("apiKey")
        firebaseConfig = {
            "apiKey": self.api_key,
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
            print("Email: ", email)
            print("UID: ", login["localId"])
            return login["localId"], True
        except:
            print("Invalid Email or Password")
            return "", False

    def signup_user(self, email, password):
        try:
            user = self.auth.create_user_with_email_and_password(email, password)
            print("Email: ", email)
            print("UID: ",user["localId"])
            return user["localId"], True
        except:
            print("Email already exists")
            return "", False

    def google_login(self):
        SCOPES = [
            "openid",
            "https://www.googleapis.com/auth/userinfo.email",
            "https://www.googleapis.com/auth/userinfo.profile"
        ]


        # Start Google login
        flow = InstalledAppFlow.from_client_secrets_file("client_secret.json",SCOPES)
        credentials = flow.run_local_server(port=0)
        google_id_token = credentials.id_token

        url = (
            "https://identitytoolkit.googleapis.com/v1/"
            f"accounts:signInWithIdp?key={self.api_key}"
        )


        data = {
            "postBody": f"id_token={google_id_token}&providerId=google.com",
            "requestUri": "http://localhost",
            "returnSecureToken": True,
            "returnIdpCredential": True
        }


        response = requests.post(url, json=data)
        result = response.json()
        print("Logged In: ", result.get("email"))
        print("UID: ", result.get("localId"))
        return result.get("localId"), True