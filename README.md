# asterisk-sms-to-gnucash
Create transactions via text-messagging to a listening asterisk server and gnucash.

## Examples: 
### Defaulting as Credit Card Expense:
```"Books,The Martian,$9.00"```

Success:  ($9.00) "The Martian" Expenses:Books from Liabilities:Credit Card

### Changing Expense to come out of Checking:
```"Movies,The Martian,$16.00,Checking"```

Success:  ($16.00) "The Martian" Expenses:Movies from Account:Checking

### Changing to Income to add into Checking:
```"Salary,Making Bank,$1,000,000,Checking, Income"```

Success:  ($1,000,000) "Making Bank" Income:Salary into Account:Checking
