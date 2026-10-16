"""Problem 101: Right-aligned alphabet triangle"""

n = int(input("Enter number of rows (up to 26): "))
for row in range(1, min(n, 26) + 1):
    print(" " * (n - row) + "".join(chr(65 + col) for col in range(row)))
