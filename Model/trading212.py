from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

import pandas as pd
import requests
import os

class Trading212:
    def __init__(self):
        load_dotenv()
        self.API_KEY = os.getenv("TRADING212_API_KEY_ID")
        self.API_SECRET = os.getenv("TRADING212_SECRET_KEY")

        url = "https://live.trading212.com/api/v0/equity/portfolio"
        self.portfolio_response = requests.get(url,auth=HTTPBasicAuth(self.API_KEY, self.API_SECRET))


    def getUPL(self):
        if(self.portfolio_response.status_code == 200):
            data = self.portfolio_response.json()[0]
            return data["ppl"]
        return 0

    def getDatesDepositsPortValue(self):
        BASE_URL = "https://live.trading212.com"
        next_path = "/api/v0/equity/history/orders?limit=50"
        items = []
        while next_path:
            response = requests.get(BASE_URL + next_path,auth=HTTPBasicAuth(self.API_KEY, self.API_SECRET))
            response.raise_for_status()

            data = response.json()

            items.extend(data["items"])
            next_path = data.get("nextPagePath")

        fills = []
        orders = []
        for item in items:
            if("fill" in item.keys()):
                order = item["order"]
                fill = item["fill"]
                del fill["walletImpact"]
                fills.append(fill)
                orders.append(order)

        fill_df = pd.DataFrame(fills).sort_values(by="filledAt")
        fill_df = fill_df[["quantity", "price"]]
        order_df = pd.DataFrame(orders).sort_values(by="createdAt")
        order_df = order_df[["value", "createdAt"]]

        order_df["cumValue"] = order_df["value"].cumsum()
        df = pd.concat([order_df, fill_df], axis=1)
        df["cumQuantity"] = df["quantity"].cumsum()
        df["price"] *= 1.16
        df["portfolioValue"] = df["cumQuantity"] * df["price"]
        return df["createdAt"].tolist(), df["cumValue"].tolist(), df["portfolioValue"].tolist()
