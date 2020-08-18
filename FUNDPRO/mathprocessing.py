import math

fraction = float(input("Enter the fraction of carbon-14: "))

while fraction < 0 or fraction > 1:
    print("\nA fraction should be a number between 0 and 1.\nPlease try again\n")
    fraction = float(input("Enter the fraction of carbon-14: "))

c14frac = round(math.log10(1 / fraction) / 0.00012, 2)

print(f"\nThe specimen is {c14frac} years old.")
