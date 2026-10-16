"""Problem 097: Binary number triangle"""

n = int(input("Enter number of rows: "))
for row in range(1, n + 1):
    for col in range(row):
        print(0 if col % 2 == 0 else 1, end="")
    print()
