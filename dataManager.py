from io import BytesIO

import requests
import pandas as pd



class Finances:
    def __init__(self, accountBalance, cashBalance, df):
        self.accountBalance = accountBalance*100
        self.cashBalance = cashBalance*100
        self.df = df
        self.df["Amount"] *= 100

    def getAccountBalanceToDate(self):
        accountTrans = self.df[(self.df["Payment Method"] == "Card") | (self.df["Payment Method"] == "Bank Transfer") | (self.df["Payment Method"] == "Cheque")]
        return (self.accountBalance + accountTrans["Amount"].sum())/100

    def getCashBalanceToDate(self):
        cashTrans = self.df[self.df["Payment Method"] == "Cash"]
        return (self.cashBalance + cashTrans["Amount"].sum())/100

    def getInvestmentDeposits(self):
        deposited = self.df[self.df["Category"] == "Investing"]
        return (deposited["Amount"].sum())*-1/100

    def getRecentTransactions(self, num):
        print(self.df["Category"].unique())
        last = self.df.tail(num)
        last["Amount"] /= 100
        return last.to_dict("index")





def getGoogleSheet():
    r = requests.get('https://docs.google.com/spreadsheet/ccc?key=1zNKPjLWWRia4eNqX5SIUx67sBXv8y_Bq0d3YU8zxeO8&output=csv')
    return BytesIO(r.content)

def getCSV():
    return "allData.csv"

def getDataframe():
    df = pd.read_csv(getCSV())
    df = df[["Date", "Amount", "Payment Method", "Shop/Person", "Location", "Description", "Category"]]
    df["Date"] = pd.to_datetime(df["Date"], format="%d-%b-%Y")
    df = df.sort_values("Date")
    return df;

def getFinances():
    return Finances(4423.71, 120.00, getDataframe())