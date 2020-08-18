def print_function(n):
    if n < 1:
        return 1
    else:
        print(n, end=" ")
        print_function(n-1)
        print(n, end=" ")
        return


num = 3

print_function(3)
