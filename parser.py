import sys
from transaction import transaction, add_transaction

#parseList = ['Dining,Pizza Place,$10.00']
#parseList.append('Movie,The Martian,$16.66,Checking')
#parseList.append('Gift,Gift Card,$50.00,Checking,Income')

for a in range(1,len(sys.argv)):
    i = sys.argv[a]
    splitTransaction = i.split(',')
    length = len(splitTransaction)
    
    if length >= 3:
        t = transaction(splitTransaction[1], splitTransaction[2],splitTransaction[0])
    if length >= 4 :
        t = transaction(splitTransaction[1], splitTransaction[2],splitTransaction[0], splitTransaction[3])
        t.account = splitTransaction[3]
    if length >= 5 and splitTransaction[4] == 'Income':
        t = transaction(splitTransaction[1], splitTransaction[2],splitTransaction[0], splitTransaction[3], True) 

    add_transaction(t)
    