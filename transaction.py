from piecash import open_book, Transaction, Split
from datetime import datetime
from decimal import Decimal

# reopen the book and add a transaction
# this must be a sqlite3 file
with open_book("./sample.gnucash",
               open_if_lock=True,
               readonly=False) as mybook:
    today = datetime.now()
    # retrieve the currency from the book
    USD = mybook.currencies(mnemonic="USD")
    
    # define the amount as Decimal
    amount = Decimal("100.00")
    
    # retrieve accounts
    to_account = mybook.accounts(fullname="Expenses:Miscellaneous")
    from_account = mybook.accounts(fullname="Liabilities:Credit Card")
    
    # create the transaction with its two splits
    Transaction(
        post_date=today,
        enter_date=today,
        currency=USD,
        description="This is a test.",
        splits=[
            Split(account=to_account,
                  value=amount,
                  memo="Split Memo!"),
            Split(account=from_account,
                  value=-amount,
                  memo="Other Split Memo!"),
        ]
    )
    
    # save the book
    mybook.save()
