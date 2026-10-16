"""Problem 105: Number diamond"""

n = int(input("Enter half-height of number diamond: "))
for row in range(1, n + 1):
    print(" " * (n - row) + "".join(str(i) for i in range(1, row + 1)) + "".join(str(i) for i in range(row - 1, 0, -1)))
for row in range(n - 1, 0, -1):
    print(" " * (n - row) + "".join(str(i) for i in range(1, row + 1)) + "".join(str(i) for i in range(row - 1, 0, -1)))
