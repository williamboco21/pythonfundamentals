month: int = int(input("Enter the month of your birthday: "))
day = int(input("Enter the day of your birthday: "))

if (month == 3 and (21 <= day <= 31)) or (month == 4 and (1 <= day <= 19)):
    print("Your horoscope sign is Aries.")
elif (month == 4 and (20 <= day <= 30)) or (month == 5 and (1 <= day <= 20)):
    print("Your horoscope sign is Taurus.")
elif (month == 5 and (21 <= day <= 31)) or (month == 6 and (1 <= day <= 21)):
    print("Your horoscope sign is Gemini.")
elif (month == 6 and (22 <= day <= 30)) or (month == 7 and (1 <= day <= 22)):
    print("Your horoscope sign is Cancer.")
elif (month == 7 and (23 <= day <= 31)) or (month == 8 and (1 <= day <= 22)):
    print("Your horoscope sign is Leo.")
elif (month == 8 and (23 <= day <= 31)) or (month == 9 and (1 <= day <= 22)):
    print("Your horoscope sign is Virgo.")
elif (month == 9 and (23 <= day <= 30)) or (month == 10 and (1 <= day <= 23)):
    print("Your horoscope sign is Libra.")
elif (month == 10 and (24 <= day <= 31)) or (month == 11 and (1 <= day <= 21)):
    print("Your horoscope sign is Scorpio.")
elif (month == 11 and (22 <= day <= 30)) or (month == 12 and (1 <= day <= 21)):
    print("Your horoscope sign is Sagittarius.")
elif (month == 12 and (22 <= day <= 31)) or (month == 1 and (1 <= day <= 19)):
    print("Your horoscope sign is Capricorn.")
elif (month == 1 and (20 <= day <= 31)) or (month == 2 and (1 <= day <= 18)):
    print("Your horoscope sign is Aquarius.")
elif (month == 2 and (19 <= day <= 28)) or (month == 3 and (1 <= day <= 20)):
    print("Your horoscope sign is Pisces.")
else:
    print("You entered an invalid date! Program Terminating!")