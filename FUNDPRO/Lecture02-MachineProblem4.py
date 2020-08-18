import speedoflight

# Speed of Light Conversion
distance = float(input("Enter the mass of the object in kilograms: "))
energy = distance * speedoflight.SPEED
print(f'If the mass is {distance} kg,'
      f'then the energy produced is '
      f'{energy} joules.')