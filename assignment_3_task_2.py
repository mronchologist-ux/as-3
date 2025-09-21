
'''Task 2: Using the Math Module for Calculations
Problem Statement: Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)
3.   Displays the calculated results.'''

x = float(input("enter the number: "))
import math
print()
sqrt_val = math.sqrt(x)
log_val = math.log(x)
sine_val = math.sin(x)
print(f"Square root = {sqrt_val}")
print(f"logarithm = {log_val}")
print(f"sine = {sine_val}")

    