"""Problem 104: Hollow diamond inside rectangle"""

n = int(input("Enter half-height of hollow diamond: "))
width = 2 * n + 1
for row in range(n + 1):
    inner = 2 * row - 1
    if row == 0:
        print("*" * width)
    else:
        print("**" + " " * inner + "*" * (width - inner - 2))
for row in range(n - 1, -1, -1):
    inner = 2 * row - 1
    if row == 0:
        print("*" * width)
    else:
        print("**" + " " * inner + "*" * (width - inner - 2))
