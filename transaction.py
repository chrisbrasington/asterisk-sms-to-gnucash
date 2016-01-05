from piecash import open_book, Transaction, Split
from datetime import datetime
from decimal import Decimal

class transaction:
    name = ''
    amount = 0.00
    expense = 'Imbalance'
    account = 'Credit Card'
    income = False
    
    def __init__(self, name, amount, expense = 'Imbalance', account = 'Credit Card', income = False):
        self.name = name
        self.amount = Decimal(amount.strip('$'))

        # allow for shorthand of 'Credit Card' as 'CC'
        if(account == 'CC'):
            acount == 'Credit Card'
        
        # from account:
        #   want to prefix either 'Liabilities:' or 'Account:' on the from_account
        #   unless explicitly stated in message
        if 'Liabilities:' not in account or 'Account:' not in account:
            if(account == 'Credit Card'):
                account = 'Liabilities:' + account
            else:
                account = 'Account:' + account
        
        # to account: 
        #   want to prefix either 'Expense:' or 'Income:' on the to_account
        #   unless explicitly stated in message
        if 'Income:' not in account or 'Expenses:' not in account:
            if(income):
                expense = 'Income:' + expense
            else:
                expense = 'Expenses:' + expense
                
        self.expense = expense
        self.account = account
        self.income = income
        
    def __str__(self):
        s = ('($' + str(self.amount) + ') "'+ self.name+'" ')
        s += self.expense
        if self.income:
            s += " into "
        else:
            s += " from "
        s += self.account
        return s

def add_transaction(t):
    success = True
    
    try: 
        # reopen the book and add a transaction
        # this must be a sqlite3 file
        with open_book('./sample.gnucash',
                    open_if_lock=True,
                    readonly=False) as mybook:
            today = datetime.now()
            today = today.replace(microsecond = 0)
            
            # retrieve the currency from the book
            USD = mybook.currencies(mnemonic='USD')
            
            # define the amount as Decimal
            amount = t.amount
            
            # retrieve accounts
            to_account = mybook.accounts(fullname=t.expense)
            from_account = mybook.accounts(fullname=t.account)
            
            # create the transaction with its two splits
            Transaction(
                post_date=today,
                enter_date=today,
                currency=USD,
                description=t.name,
                splits=[
                    Split(account=to_account,
                        value=amount,
                        memo='Automated from script'),
                    Split(account=from_account,
                        value=-amount,
                        memo='Automated from script'),
                ]
            )
            
            # save the book
            mybook.save()
    except:
        success = False
    finally:
        log(success, t)

def log(success, t):
    if success:
        message = 'Success: '
    else:
        message = 'FAILURE: '
    message += datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' '
    message += str(t) + '\n'
    
    print message,
    
    with open("sms-transaction.log", "a") as myfile:
        myfile.write(message)

