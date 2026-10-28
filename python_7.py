matrix = [
    [3, -1, 7],
    [-4, 2, 6],
    [8, 0, -2]
]

print("Original Matrix:")
for row in matrix:
    print(row)

filtered_matrix = [
    list(filter(lambda value: value >= 0, row))
    for row in matrix
]

print("\nMatrix After Filtering Negative Values:")
for row in filtered_matrix:
    print(row)

transformed_matrix = [
    list(map(lambda value: value * 2, row))
    for row in filtered_matrix
]

print("\nMatrix After Doubling Values:")
for row in transformed_matrix:
    print(row)

sorted_matrix = [
    sorted(row, key=lambda value: -value)
    for row in transformed_matrix
]

print("\nSorted Matrix Rows:")
for row in sorted_matrix:
    print(row)
