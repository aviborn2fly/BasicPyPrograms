price = 1000000
credit = True
if credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print (f'Down Payment is :{down_payment}')