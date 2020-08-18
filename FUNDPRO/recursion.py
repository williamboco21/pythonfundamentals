def count_down(n):
    if n != 0:
        print(f"{n}!", end=" ")
        count_down(n-1)
    else:
        print("\nBLAST OFF")

count_down(5)
