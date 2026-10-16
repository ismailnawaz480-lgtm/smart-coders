"""Problem 107: Spiral number matrix (4×4)"""

# The 4x4 spiral number matrix shown in the assignment.
matrix = [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7],
]
for row in matrix:
    print(" ".join(f"{number:2}" for number in row))
