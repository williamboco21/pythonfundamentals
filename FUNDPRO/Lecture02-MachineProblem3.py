import kilometer

distance = float(input("Enter the distance in kilometers: "))
miles = kilometer.KILOMETER * distance
print(f'If the distance is '
      f'{distance} km, then it is '
      f'equivalent to {miles} miles.')