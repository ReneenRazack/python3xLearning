# Task - Factorial of a number
# Write a python program for finding Factorial of a number.

# n = 5
# 5! -->5*4*3*2*1 -> 120
# 3! -> 3*2*1 -> 6
# 4! -> 4*3*2*1 -> 24

# Input the number from the user
num = int(input("Enter a number: "))

# Initialize the factorial variable to 1
factorial = 1

# Calculate the factorial using a for loop
for i in range(1, num + 1):
    factorial *= i

# Print the result
print(f"The factorial of {num} is {factorial}.")