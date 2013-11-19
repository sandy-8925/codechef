withdraw_amount,bank_balance = raw_input().split()

bank_transaction_charge = float(0.50)

withdraw_amount = int(withdraw_amount)
bank_balance = float(bank_balance)

debit_amount = withdraw_amount + bank_transaction_charge

if withdraw_amount%5==0 and debit_amount<=bank_balance:
  bank_balance -= debit_amount

print ("%.2f" % bank_balance)