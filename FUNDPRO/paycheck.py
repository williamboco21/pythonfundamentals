BONUS1 = 500
BONUS2 = 1000
COMMISSION1 = 0.03
COMMISSION2 = 0.06

base_salary = int(input("Enter your base salary: "))
years = int(input("Enter the number of years of service: "))
total_sales = int(input("Enter the total sales: "))

if years <= 5:
    bonus = years * BONUS1
else:
    bonus = years * BONUS2

if total_sales < 50000:
    commission = total_sales * COMMISSION1
else:
    commission = total_sales * COMMISSION2

total_paycheck = int(base_salary + bonus + commission)

print(f'\nThe total paycheck is {total_paycheck} pesos.')
