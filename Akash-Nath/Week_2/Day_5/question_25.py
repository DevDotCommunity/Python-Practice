#Task: Write a program that calculates the area of a sector in a circle. (Variables, Basic Arithmetic)
from math import pi

def find_area(angle, radius):
    area = (angle)/360*pi*(radius**2)
    return area

angle = int(input("Enter the angle created in the center of the circle: "))
radius = int(input("Enter the radius of the circle: "))

area = find_area(angle, radius)

print(f"Area is {area}")