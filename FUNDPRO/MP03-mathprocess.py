def comp_int(x, y, z):
    term = pow(1 + (x / y), y * z)

    return term


def comp_bal(w, x, y, z):
    return w * comp_int(x, y, z)


w = int(input("Enter the value for w: "))
x = float(input("Enter the value for x: "))

while x < 0 or x > 1:
    print("\nThe value of x should be between 0 and 1 only. Please try again.\n")
    x = float(input("Enter the value for x: "))

y = int(input("Enter the value for y: "))
z = int(input("Enter the value for z: "))


balance = round(comp_bal(w, x, y, z), 2)

print(f"\nThe balance is {balance} pesos.")
