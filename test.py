import pyrebase

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
auth=firebase.auth()

def login():
    print("Log in...")
    email = input("Enter email: ")
    password = input("Enter password: ")
    try:
        login = auth.sign_in_with_email_and_password(email, password)
        print("Successfully logged in!")
        print(login)
    except:
        print("invalid email or password")

def signup():
    print("Sign up...")
    email = input("Enter email: ")
    password = input("Enter password: ")

    try:
        user = auth.create_user_with_email_and_password(email, password)
    except:
        print("Email already exists")

ans = input("New User?? [y/n]")

if(ans == "n"):
    login()
else:
    signup()