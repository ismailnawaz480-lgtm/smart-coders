"""Problem 092: Pascal's triangle"""

n = int(input("Enter number of rows: "))
for row in range(n):
    print(" " * (n - row - 1), end="")
    value = 1
    for col in range(row + 1):
        print(value, end=" ")
        value = value * (row - col) // (col + 1) if col < row else value
    print()
