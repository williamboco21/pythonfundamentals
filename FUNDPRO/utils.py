def find_max(num):
    maximum = num[0]

    for h in num:
        if h > maximum:
            maximum = h

    return maximum
