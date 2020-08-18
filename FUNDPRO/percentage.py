original_value = int(input("Enter the original value: "))
new_value = int(input("Enter the new value: "))
percentage = None

if new_value > original_value:
    percentage = ((new_value - original_value) / original_value) * 100
    print(f'The value increase and the percent ')
elif new_value < original_value:
    percentage = ((original_value - new_value) / original_value) * 100
else:
    print("The value did not change.")

print(f'The value increased and the percent increase is {percentage}%.')