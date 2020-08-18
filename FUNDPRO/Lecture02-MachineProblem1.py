import gravity

first_mass = float(input("The mass of the first object: "))
second_mass = float(input("The mass of the second object: "))
distance = float(input("Enter the distance between the two objects: "))
distance = pow(distance, 2)


gravitational_force = ((gravity.GRAVITY * first_mass * second_mass) / distance)

print("\nThe gravitational force is", gravitational_force)