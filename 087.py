"""Problem 087: Sandglass / Hourglass"""

n = int(input("Enter half-height of sandglass: "))
for row in range(n, 0, -1):
    print(" " * (n - row) + "*" * (2 * row - 1))
for row in range(2, n + 1):
    print(" " * (n - row) + "*" * (2 * row - 1))
