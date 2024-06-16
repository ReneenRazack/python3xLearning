# Write a python program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# Determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).

# Use an if-else statement to classify the triangle.

# 3 Inputs
# side 1, side 2 and side 3
# output - Eq, Iso, Scalene -
# Eq. = side 1 == side 2 = side 3

# Input the lengths of the sides from the user
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Classify the triangle
if side1 == side2 == side3:
    print("Equilateral")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("Isosceles")
else:
    print("Scalene")