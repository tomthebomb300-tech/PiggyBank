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

        self.filled_order_df = None
        self.createFilledOrderDF()

    def getUPL(self):
        if(self.portfolio_response.status_code == 200):
            data = self.portfolio_response.json()[0]
            return data["ppl"]
        return 0


    def createFilledOrderDF(self):
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
        order_df = pd.DataFrame(orders).sort_values(by="createdAt")

        fill_df.drop("id", axis="columns", inplace=True)
        fill_df.drop("type", axis="columns", inplace=True)

        order_df["cumValue"] = order_df["value"].cumsum()
        self.filled_order_df = pd.concat([order_df, fill_df], axis=1)
        self.filled_order_df["cumQuantity"] = self.filled_order_df["quantity"].cumsum()
        self.filled_order_df["portfolioValue"] = self.filled_order_df["cumQuantity"] * (self.filled_order_df["price"] * 1.16)


    def getDatesDepositsPortValue(self):
        return self.filled_order_df["filledAt"].tolist(), self.filled_order_df["cumValue"].tolist(), self.filled_order_df["portfolioValue"].tolist()

    def getFilledOrderDetailsDict(self):
        return self.filled_order_df[["type", "filledValue", "initiatedFrom", "instrument", "quantity", "price", "filledAt", "side"]].to_dict("index")
