def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * (tip_percent / 100)
    tax = meal_cost * (tax_percent / 100)
    totalcost = meal_cost + tip + tax

    return totalcost

meal_cost = float(input())
tip_percent = float(input())
tax_percent = float(input())

total_cost = solve(meal_cost, tip_percent, tax_percent)

print(round(total_cost))