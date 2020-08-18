def convert(dollar):
    return float(dollar * 50.98)


usd = float(input("Enter the amount in dollars: "))

php = round(convert(usd), 2)

print(f"\nThe amount in pesos is {php}.")
