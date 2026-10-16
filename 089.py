"""Problem 089: Sequential number triangle"""

n = int(input("Enter number of rows: "))
number = 1
for row in range(1, n + 1):
    values = []
    for _ in range(row):
        values.append(str(number))
        number += 1
    print(" ".join(values))
