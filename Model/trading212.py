from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

import requests
import os

class Trading212:
    def __init__(self):
        load_dotenv()
        self.API_KEY = os.getenv("TRADING212_API_KEY_ID")
        self.API_SECRET = os.getenv("TRADING212_SECRET_KEY")

    def getUPL(self):
        url = "https://live.trading212.com/api/v0/equity/portfolio"
        
        response = requests.get(url,auth=HTTPBasicAuth(self.API_KEY, self.API_SECRET))
        if(response.status_code == 200):
            data = response.json()[0]
            return data["ppl"]
        return 0