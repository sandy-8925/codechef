import re
input_data = re.split('\s',raw_input())

bank_charge = 0.50

withdraw_amount = int(input_data[0])
bank_balance = float(input_data[1])

debit_amount = withdraw_amount + bank_charge

if withdraw_amount%5==0 and debit_amount <= bank_balance:
  bank_balance -= debit_amount

print ("%.2f" % bank_balance)

exit(0)