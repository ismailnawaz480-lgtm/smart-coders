"""Problem 108: Right arrow pattern"""

n = int(input("Enter arrow size (at least 2): "))
for row in range(1, n + 1):
    if row <= n // 2:
        print("*")
    elif row == n // 2 + 1:
        print("* " * n)
    else:
        print("*")
