"""Problem 094: Inverted number triangle"""

n = int(input("Enter number of rows: "))
for row in range(n, 0, -1):
    print("".join(str(i) for i in range(1, row + 1)))
