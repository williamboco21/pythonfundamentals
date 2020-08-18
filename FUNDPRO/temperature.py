print(f'TEMPERATURE CONVERSION PROGRAM')
print(f'------------------------------\n')
print("Options:\n")
print(f'1. Convert Celsius to Fahrenheit\n'
      f'2. Convert Fahrenheit to Celsius\n'
      f'3. Exit Program\n')

choice = int(input("Enter your choice: "))

if choice == 1:
    celsius = int(input("\nEnter temperature in Celsius: "))
    fahrenheit = (9 / 5) * celsius + 32
    print(f'\nThe temperature in Celsius is {fahrenheit}.\n')
elif choice == 2:
    fahrenheit = int(input("\nEnter temperature in Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print(f'\nThe temperature in Celsius is {celsius}.\n')
elif choice == 3:
    print("\nProgram Exiting!\n")
    print("Thank you for using this program!")
    exit()
else:
    print("\nInvalid entry! Please try again!\n")


print("Thank you for using this program!")