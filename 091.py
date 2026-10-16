"""Problem 091: 1-0 alternating triangle"""

n = int(input("Enter number of rows: "))
for row in range(1, n + 1):
    for col in range(row):
        print(1 if col % 2 == 0 else 0, end="")
    print()
