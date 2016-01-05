import sys

class transaction:
    name = ""
    amount = 0.00
    expense = "Imbalance"
    account = "Credit Card"
    income = False
    
    def __init__(self, name, amount, expense):
        self.name = name
        self.amount = amount
        self.expense = expense
    def __str__(self):
        s = ("(" + str(self.amount) + ") "+ self.name + " - " + self.expense 
            + " from " + self.account)
        if(self.income):
            s += " (as income)"
        else:
            s += " (as expense)"
        return s

#parseList = ["Dining,Pizza Place,$10.00"]
#parseList.append("Movie,The Martian,$16.66,Checking")
#parseList.append("Gift,Gift Card,$50.00,Checking,Income")

for a in range(1,len(sys.argv)):
    i = sys.argv[a]
    splitTransaction = i.split(",")
    length = len(splitTransaction)
    
    if length >= 3:
        t = transaction(splitTransaction[1], splitTransaction[0],splitTransaction[2])
        if length >= 4 :
            t.account = splitTransaction[3]
        if length >= 5 and splitTransaction[4] == "Income":
            t.income = True 
        
        print t
    