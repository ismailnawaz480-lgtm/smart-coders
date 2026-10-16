"""Problem 088: Number triangle (row-wise)"""

n = int(input("Enter number of rows: "))
for row in range(1, n + 1):
    print(str(row) * row)
