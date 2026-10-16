"""Problem 109: X pattern"""

n = int(input("Enter an odd size for the X pattern: "))
if n % 2 == 0:
    print("Please enter an odd number")
else:
    for row in range(n):
        for col in range(n):
            print("*" if col == row or col == n - row - 1 else " ", end="")
        print()
