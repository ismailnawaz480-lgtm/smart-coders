"""Problem 081: Inverted right-aligned triangle"""

n = int(input("Enter number of rows: "))
for row in range(n, 0, -1):
    print(" " * (n - row) + "*" * row)
