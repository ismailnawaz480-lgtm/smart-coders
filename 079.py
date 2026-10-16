"""Problem 079: Inverted right-angled triangle"""

n = int(input("Enter number of rows: "))
for row in range(n, 0, -1):
    print("*" * row)
