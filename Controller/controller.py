from Model.dataManager import getFinances

class Controller:
    def __init__(self):
        self.finances = getFinances()

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