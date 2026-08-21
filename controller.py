from dataManager import getFinances

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