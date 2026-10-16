"""Problem 084: Diamond shape"""

n = int(input("Enter half-height of diamond: "))
for row in range(1, n + 1):
    print(" " * (n - row) + "*" * (2 * row - 1))
for row in range(n - 1, 0, -1):
    print(" " * (n - row) + "*" * (2 * row - 1))
