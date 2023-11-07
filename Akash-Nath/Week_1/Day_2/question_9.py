#Task: Write a program that converts temperature from Fahrenheit to Celsius. (Variables, Basic Arithmetic)

"""
C/5 = (F-32)/9
=> C = (F-32)*5/9
"""

fahrenheit = int(input("Enter the fahrenheit value: "))

celcius = (fahrenheit-32)*5/9

print(f"{fahrenheit} fahrenheit = {celcius} celcius")