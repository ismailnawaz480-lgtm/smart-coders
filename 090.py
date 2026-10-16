"""Problem 090: Floyd's triangle"""

n = int(input("Enter number of rows: "))
number = 1
for row in range(1, n + 1):
    for _ in range(row):
        print(number, end=" ")
        number += 1
    print()
