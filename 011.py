"""Problem 011: Check if a number is even or odd using bitwise AND ( n & 1 )"""

n = int(input("Enter an integer: "))
if n & 1:
    print("Odd")
else:
    print("Even")
