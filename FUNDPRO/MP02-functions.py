def gross_pay(hour):
    hourly_rate = 500
    if hour > 40:
        ot = (hour - 40) * 1.5 * hourly_rate
        gross = 40 * hourly_rate + ot
    else:
        gross = hour * hourly_rate

    return int(gross)


def social_security_tax(gross):
    return gross * 0.015


def hdmf_contribution(gross):
    return gross * 0.03


def professional_income_tax(gross):
    return int(gross * 0.10)


def health_insurance(dependent):
    if dependent > 2:
        health = 300
    else:
        health = 0

    return health


hours = int(input("Enter the number of hours worked: "))
dependents = int(input("Enter the number of dependent/s: "))

gross_pay = gross_pay(hours)
insurance = health_insurance(dependents)

sst = social_security_tax(gross_pay)
hdmf = hdmf_contribution(gross_pay)
pit = professional_income_tax(gross_pay)

net_pay = gross_pay - sst - hdmf - pit - insurance

print(f"Gross Pay = {gross_pay} pesos\n"
      f"\nSocial Security Tax = {sst} pesos"
      f"\nHDMF = {hdmf} pesos"
      f"\nProfessional Income Tax = {pit} pesos"
      f"\nHealth Insurance = {insurance} pesos\n"
      f"\nNet Take Home Pay for the week = {round(net_pay, 1)} pesos.")

