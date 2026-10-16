"""Problem 112: Square with diagonals marked"""

n = int(input("Enter square size (at least 3): "))
for row in range(n):
    for col in range(n):
        if row == 0 or row == n - 1 or col == 0 or col == n - 1 or row == col or row + col == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
