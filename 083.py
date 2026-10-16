"""Problem 083: Inverted pyramid"""

n = int(input("Enter number of rows: "))
for row in range(n, 0, -1):
    print(" " * (n - row) + "*" * (2 * row - 1))
