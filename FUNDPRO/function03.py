def magic1(y):
    print(f"The value of x in the function is {y}.")
    y = 10
    print(f"The value of x after changing the value is {y}.\n")


x = 5

print(f"The value of x before passing to a function is {x}.\n")
magic1(x)
print(f"The value of x is still {x}.")
