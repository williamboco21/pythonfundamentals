price = 1000000
good_credit = True

if good_credit:
    down_pay = price * 0.1
else:
    down_pay = price * 0.2

print(f"Downpayment is ${down_pay}")