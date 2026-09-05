from io import BytesIO
from datetime import datetime

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
        last = self.df.tail(num)
        last["Amount"] /= 100
        return last.to_dict("index")

    def getBiggestExpenses(self, month, year):
        month = self.df[(self.df["Date"].dt.year == year) & (self.df["Date"].dt.month == month)]
        categorys = self.df["Category"].unique()
        dict = {}
        for c in categorys:
            expense = month[(month["Category"] == c) & (month["Amount"] < 0)]["Amount"].sum()
            if(expense < 0):
                dict[c] = expense/100

        if(len(dict) <= 5):
            return dict

        #Hold 5 largest expenses and compact all others into one category        
        other = 0
        while(len(dict) > 5):
            smallestExpense = -100000
            smallestCategory = None
            for key in dict:
                if(dict[key] > smallestExpense):
                    smallestExpense = dict[key]
                    smallestCategory = key
            other += smallestExpense
            del dict[smallestCategory]
        dict["Other"] = round(other, 2)
        
        return dict

    def getMonths(self, year):
        month_nums = self.df[self.df["Date"].dt.year == year]["Date"].dt.month.unique()

        months = []
        for num in month_nums:
            months.append(datetime(year, num, 1).strftime("%b"))
        return months

    def getMonthlyAccountBalance(self, year):
        #Account account balance at start of year
        prev_years_df = self.df[self.df["Date"].dt.year < year]
        account_balance = prev_years_df[
            (prev_years_df["Payment Method"] == "Card") |
            (prev_years_df["Payment Method"] == "Bank Transfer") |
            (prev_years_df["Payment Method"] == "Cheque")
        ]["Amount"].sum() + self.accountBalance

        year_df = self.df[self.df["Date"].dt.year == year]
        month_nums = year_df["Date"].dt.month.unique()

        monthly_account_balance = []
        for num in month_nums:
            month_df = year_df[year_df["Date"].dt.month == num]
            month_balance = month_df[
                (month_df["Payment Method"] == "Card") | 
                (month_df["Payment Method"] == "Bank Transfer") | 
                (month_df["Payment Method"] == "Cheque")]["Amount"].sum()
            account_balance += month_balance
            monthly_account_balance.append(round(account_balance/100, 2))
        return monthly_account_balance

    def getMonthlyCashBalance(self, year):
        #Account cash balance at start of year
        prev_years_df = self.df[self.df["Date"].dt.year < year]
        cash_balance = prev_years_df[prev_years_df["Payment Method"] == "Cash"]["Amount"].sum() + self.cashBalance

        year_df = self.df[self.df["Date"].dt.year == year]
        month_nums = year_df["Date"].dt.month.unique()

        monthly_cash_balance = []
        for num in month_nums:
            month_df = year_df[year_df["Date"].dt.month == num]
            month_balance = month_df[month_df["Payment Method"] == "Cash"]["Amount"].sum()
            cash_balance += month_balance
            monthly_cash_balance.append(round(cash_balance/100, 2))
        return monthly_cash_balance

    def getMonthlyInvestedBalance(self, year):
        #Invested money at start of year
        prev_years_df = self.df[self.df["Date"].dt.year < year]
        invested_balance = prev_years_df[prev_years_df["Category"] == "Investing"]["Amount"].sum()

        year_df = self.df[self.df["Date"].dt.year == year]
        month_nums = year_df["Date"].dt.month.unique()

        monthly_invested_balance = []
        for num in month_nums:
            month_df = year_df[year_df["Date"].dt.month == num]
            month_balance = month_df[month_df["Category"] == "Investing"]["Amount"].sum()
            invested_balance += month_balance
            monthly_invested_balance.append(round(invested_balance/100, 2)*-1)
        return monthly_invested_balance

    def getCategories(self):
        return self.df["Category"].unique()

    def getIncome(self, category):
        return self.df[(self.df["Category"] == category) & (self.df["Amount"] > 0)]["Amount"].sum()/100

    def getExpense(self, category):
        return self.df[(self.df["Category"] == category) & (self.df["Amount"] < 0)]["Amount"].sum()/100

    def getStartDate(self):
        return self.df["Date"].iloc[0]

    def getLastDate(self):
        return self.df["Date"].iloc[len(self.df)-1]





def getGoogleSheet():
    r = requests.get('https://docs.google.com/spreadsheet/ccc?key=1zNKPjLWWRia4eNqX5SIUx67sBXv8y_Bq0d3YU8zxeO8&output=csv')
    return BytesIO(r.content)

def getCSV():
    return "D:\Coding\Python\PiggyBank\Data\data.csv"

def getDataframe():
    df = pd.read_csv(getCSV())
    # df = pd.read_csv(getGoogleSheet())
    # df.to_csv("Data.csv")
    df = df[["Date", "Amount", "Payment Method", "Shop/Person", "Location", "Description", "Category"]]
    df["Date"] = pd.to_datetime(df["Date"], format="%d-%b-%Y")
    df = df.sort_values("Date")
    return df

def getFinances():
    return Finances(4423.71, 120.00, getDataframe())