"""Problem 110: Plus (+) pattern"""

n = int(input("Enter an odd size for the plus pattern: "))
if n % 2 == 0:
    print("Please enter an odd number")
else:
    middle = n // 2
    for row in range(n):
        for col in range(n):
            print("*" if row == middle or col == middle else " ", end="")
        print()
