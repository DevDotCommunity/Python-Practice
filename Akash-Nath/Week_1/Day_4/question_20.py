#Task: Write a program that calculates the volume of a sphere. (Variables, Basic Arithmetic)

from math import pi

radius = int(input("Enter the radius of the sphere: "))

volume = 4/3*pi*(radius**3)

print(f"The volume of the sphere is {volume}")