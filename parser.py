import sys
from transaction import transaction, add_transaction

for a in range(1,len(sys.argv)):
    i = sys.argv[a]
    splitTransaction = i.split(',')
    length = len(splitTransaction)
    
    if length == 3:
        t = transaction(splitTransaction[1], splitTransaction[2],splitTransaction[0])
    if length == 4 :
        t = transaction(splitTransaction[1], splitTransaction[2],splitTransaction[0], splitTransaction[3])
    if length == 5:
        t = transaction(splitTransaction[1], splitTransaction[2],splitTransaction[0], splitTransaction[3], True) 

    add_transaction(t)
    