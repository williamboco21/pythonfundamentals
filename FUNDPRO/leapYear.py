def leapYear(year):
    leap = False

    if year % 4 == 0:
        if year % 100 != 0:
            leap = True

    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            leap = True

    return leap

year = int(input())
print(leapYear(year))