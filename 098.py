"""Problem 098: Alphabet triangle (row repeat)"""

n = int(input("Enter number of rows (up to 26): "))
for row in range(1, min(n, 26) + 1):
    print(chr(64 + row) * row)
