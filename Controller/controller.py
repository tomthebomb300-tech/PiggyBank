from Model.dataManager import getFinances
from Model.trading212 import Trading212
from View.window import Window

class Controller:
    def __init__(self):
        self.finances = getFinances()
        self.trading212 = Trading212()
        self.window = Window("Finances", 1080, 1920, self)
        self.window.run()

    def display_overview(self):
        self.window.display_page("overview")

    def display_transactions(self):
        self.window.display_page("transactions")

    def display_investments(self):
        self.window.display_page("investments")

    def getBankBalance(self):
        return self.finances.getAccountBalanceToDate()

    def getCashBalance(self):
        return self.finances.getCashBalanceToDate()

    def getInvestmentDeposits(self):
        return self.finances.getInvestmentDeposits()

    def getRecentTransactions(self):
        return self.finances.getRecentTransactions(20)

    def getBiggestExpenses(self, month, year):
        return self.finances.getBiggestExpenses(month, year)

    def getImagePath(self, transaction):
        image = "Images/Light/{0}.png"
        c = transaction["Category"]
        if(c == "BOI Fees"):
            return image.format("BOI")
        if(c == "Car"):
            return image.format("Car")
        if(c == "Clothes"):
            return image.format("Clothes")
        if(c == "Entertainment"):
            return image.format("Entertainment")
        if(c=="Food" or c=="Impulsive Food" or c=="Food Non-Personal"):
            if(transaction["Shop/Person"] == "Lidl"):
                return image.format("Lidl")
            if(transaction["Shop/Person"] == "Tesco"):
                return image.format("Tesco")
            return image.format("Food")
        if(c == "Household"):
            return image.format("Household")
        if(c == "Income"):
            return image.format("Income")
        if(c == "Investing"):
            return image.format("Investing")
        if(c == "Trading"):
            return image.format("Trading")
        if(c=="Mumsie" or c=="Dadsie" or c=="Michael" or c=="Sheila" or c=="Denis" or c=="Alexia"):
            return image.format("People")
        if(c == "Personal Development"):
            return image.format("Personal Development")
        if(c == "Personal"):
            return image.format("Personal")
        if(c == "Rent"):
            return image.format("Rent")
        if(c == "Transport"):
            return image.format("Transport")

        return "Images/Light/Null.png"

    def getMonths(self, year):
        return self.finances.getMonths(year)

    def getMonthlyAccountBalance(self, year):
        return self.finances.getMonthlyAccountBalance(year)

    def getMonthlyCashBalance(self, year):
        return self.finances.getMonthlyCashBalance(year)

    def getMonthlyInvestedBalance(self, year):
        return self.finances.getMonthlyInvestedBalance(year)

    def getPortfolioValue(self):
        return round(self.trading212.getUPL() + self.getInvestmentDeposits(),2)

    def getDatesDepositsPortValue(self):
        return self.trading212.getDatesDepositsPortValue()


    def getCategories(self):
        return self.finances.getCategories()

    def getIncome(self, categories, start_date, last_date):
        dict = {}
        for c in categories:
            income = self.finances.getIncome(c, start_date, last_date)
            if(income != 0):
                dict[c] = income
        return dict

    def getExpense(self, categories, start_date, last_date):
        dict = {}
        for c in categories:
            expense = self.finances.getExpense(c, start_date, last_date)
            if(expense != 0):
                dict[c] = expense
        return dict

    def getTransactions(self, categories, start_date, last_date):
        return self.finances.getEntries(categories, start_date, last_date)


    def getStartDate(self):
        return self.finances.getStartDate()

    def getLastDate(self):
        return self.finances.getLastDate()

    def getOHLC(self, categories, timeframe):
        return self.finances.getOHLC(categories, timeframe)

    def getWeeksAndBalances(self, categories):
        ohlc = self.finances.getOHLC(categories, "W")
        return ohlc.index.tolist(), ohlc["close"].tolist()

    def getWeeksAndInvested(self):
        ohlc = self.finances.getOHLC_investments("W")
        return ohlc.index.tolist(), ohlc["close"].ffill().tolist()