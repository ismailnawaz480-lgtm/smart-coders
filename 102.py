"""Problem 102: Alphabet pyramid (centered)"""

n = int(input("Enter number of rows (up to 13): "))
for row in range(1, min(n, 13) + 1):
    left = "".join(chr(64 + col) for col in range(1, row + 1))
    right = "".join(chr(64 + col) for col in range(row - 1, 0, -1))
    print(" " * (n - row) + left + right)
