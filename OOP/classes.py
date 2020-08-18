class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.x = 2
point1.y = 4

print(point1.x)
point1.draw()

point2 = Point()
point2.x = 1
print(point2.x)
