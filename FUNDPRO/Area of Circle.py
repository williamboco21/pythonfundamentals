import constant
import math

radius = float(input("Please enter the radius: "))
radius = math.pow(radius, 2)
area = constant.PI * radius
print("The area is", area)