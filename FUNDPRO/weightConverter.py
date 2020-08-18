weight = float(input("Weight: "))
unit = input(f"(L)bs or (K)g: ") #Chooses whether pounds or kilo

if unit.upper() == "L":
    pounds = weight // 2.205
    print(f"You are {pounds} kilos")
elif unit.upper() == "K":
    kilo = weight * 2.205
    print(f"You are {kilo} pounds.")
else:
    print("Please enter the assigned key.")
