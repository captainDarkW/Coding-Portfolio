from math import pi

print("Python can do your Geometry calculations for you!")
print("")

radius = float(input("Enter circle radius: "))

circumference = 2 * pi * radius
area_circle = pi * radius * radius

print("Circumference of the circle is", circumference)
print("Rounded to an easier number is %.2f" % circumference)
print("")
print("Area of the circle is", area_circle)
print("Rounded to an easier number is %.2f" % area_circle)
print("")

length = float(input("Enter rectangle length: "))
height = float(input("Enter rectangle height: "))
area_rectangle = length * height
perimeter = length * 2 + height * 2

print("Perimeter of the rectangle is", perimeter)
print("Rounded to an easier number is %.2f" % perimeter)
print("")
print("Area of the rectangle is", area_rectangle)
print("Rounded to an easier number is %.2f" % area_rectangle)
print("")
print("CONGRATULATIONS! Geometry homework done thanks to Python!")
