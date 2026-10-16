"""Problem 100: Reverse alphabet triangle"""

n = int(input("Enter number of rows (up to 26): "))
for row in range(min(n, 26), 0, -1):
    print("".join(chr(65 + col) for col in range(row)))
