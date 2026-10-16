"""Problem 093: Number pyramid (centered)"""

n = int(input("Enter number of rows: "))
for row in range(1, n + 1):
    print(" " * (n - row) + "".join(str(i) for i in range(1, 2 * row)))
