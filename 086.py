"""Problem 086: Hollow right-angled triangle"""

n = int(input("Enter number of rows: "))
for row in range(1, n + 1):
    for col in range(1, row + 1):
        if col == 1 or col == row or row == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()
