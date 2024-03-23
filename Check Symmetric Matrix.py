def is_symmetric(matrix):
    # Get the number of rows and columns in the matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Check if the matrix is square (number of rows == number of columns)
    if num_rows != num_cols:
        return False

    # Check if the matrix is symmetric
    for i in range(num_rows):
        for j in range(num_cols):
            if matrix[i][j] != matrix[j][i]:
                return False

    return True

# Example usage:
matrix = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

if is_symmetric(matrix):
    print("The matrix is symmetric.")
else:
    print("The matrix is not symmetric.")