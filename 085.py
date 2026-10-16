"""Problem 085: Hollow rectangle"""

rows = int(input("Enter rectangle rows (at least 2): "))
cols = int(input("Enter rectangle columns (at least 2): "))
for r in range(rows):
    for c in range(cols):
        if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
