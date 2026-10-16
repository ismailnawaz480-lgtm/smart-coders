"""Problem 082: Pyramid (centered)"""

n = int(input("Enter number of rows: "))
for row in range(1, n + 1):
    print(" " * (n - row) + "*" * (2 * row - 1))
