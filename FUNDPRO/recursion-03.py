def base_exp(base, exp):
    if exp == 0:
        return 1
    else:
        ans = base * base_exp(base, exp-1)
        return ans


base = int(input("Enter the base: "))
exp = int(input("Enter the exponent: "))

answer = base_exp(base, exp)

print(f"\nBase {base} raised to {exp} is equal to {answer}")



