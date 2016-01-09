import sys, yaml
from transaction import transaction, add_transaction

for a in range(1,len(sys.argv)):
    i = sys.argv[a]
    transactionArray = i.split(',')
    length = len(transactionArray)
    
    if length == 3:
        t = transaction(transactionArray[0], transactionArray[1],transactionArray[2])
    if length == 4 :
        t = transaction(transactionArray[0], transactionArray[1],transactionArray[2], transactionArray[3])
    if length == 5:
        t = transaction(transactionArray[0], transactionArray[1],transactionArray[2], transactionArray[3], True) 

    if length >= 3 and length <= 5:
        add_transaction(t)
