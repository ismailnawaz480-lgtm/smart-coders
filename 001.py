"""Problem 001: Read two numbers and print their sum, difference, product, quotient, and remainder"""

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
if b != 0:
    print("Quotient:", a / b)
    print("Remainder:", a % b)
else:
    print("Quotient and remainder are undefined because the second number is zero.")
