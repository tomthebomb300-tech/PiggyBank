from io import BytesIO

import requests
import pandas as pd



class Finances:
    bankBalance = 442371
    cashBalance = 12000
    df = ""

    def __init__(self, bankBalance, cashBalance, df):
        self.bankBalance = bankBalance
        self.cashBalance = cashBalance
        self.df = df





def getGoogleSheet():
    r = requests.get('https://docs.google.com/spreadsheet/ccc?key=1zNKPjLWWRia4eNqX5SIUx67sBXv8y_Bq0d3YU8zxeO8&output=csv')
    return r.content

def getDataframe():
    data = getGoogleSheet()
    df = pd.read_csv(BytesIO(data))
    df = df[["Date", "Total Balance", "Cash Balance", "Account Balance", "Amount", "Payment Method", "Shop/Person", "Location", "Description", "Category"]]
    df["Date"] = pd.to_datetime(df["Date"], format="%d-%b-%Y")
    df = df.sort_values("Date")
    df["Amount"] *= 100
    return df;

def getFinances():
    return Finances(442371, 12000, getDataframe())