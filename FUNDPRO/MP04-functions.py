def without_tax(amount):
    tax = amount * 0.12
    pesos = amount + tax

    return pesos


def with_tax(hours):
    if hours > 250:
        hours -= 250
        pesos = (hours * 9.3) + (250 * 6.2)
        bill = without_tax(pesos)
    else:
        pesos = hours * 250
        bill = without_tax(pesos)

    return bill


kilowatt_hours = int(input("Enter the number of kilowatt hours consumed: "))

print(f"\nYour electric bill is {with_tax(kilowatt_hours)} pesos.")
