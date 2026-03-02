# AIM: Design a Python program to compute the factorial of a given integer N.
# Coder: Irfan Sardar
# Date: 30-01-26

print("--- Factorial Finder ---\n")
num = int(input("Enter Number: "))

if num < 0:
    print(f"Factorial of {num} is Not Defined")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"Factorial of {num} is {factorial}")
