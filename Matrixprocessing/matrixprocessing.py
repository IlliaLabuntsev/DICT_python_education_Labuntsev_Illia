def read_matrix(size_prompt):
    """
        function read_matrix(size-prompt) - read a matrix from the user input.

        Parameters:
        - size_prompt (str): Prompt message to enter the size of the matrix in the format "rows columns".

        Returns:
        - matrix (list of lists or None): The matrix entered by the user, or None if an error occurs.

        The function prompts the user to enter the size of the matrix and then reads the matrix elements row by row.
        Each row is expected to contain numbers separated by spaces. If the row length doesn't match the specified
        number of columns, a ValueError is raised and None is returned.
    """
    try:
        user_input = input(size_prompt)
        rows, cols = map(int, user_input.split())
        matrix = []
        for _ in range(rows):
            row_input = list(map(float, input().split()))
            if len(row_input) != cols:
                raise ValueError("Invalid row length!")
            matrix.append(row_input)
        return matrix
    except ValueError as e:
        print(e)
        return None


def add_matrices(matrix_a, matrix_b):
    """
        function add_matrices(matrix_a, matrix_b) - add two matrices

        Params:
        matrix_a - the first matrix that inputted by user
        matrix_b - the second matrix that inputted by user

        Returns:
        result - the result of the addition of two matrices
    """
    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        print("The operation cannot be performed.")
        return None
    result = [[matrix_a[i][j] + matrix_b[i][j] for j in range(len(matrix_a[0]))] for i in range(len(matrix_a))]
    return result


def multiply_matrix_by_constant(matrix, constant_value):
    """
        function multiply_matrix_by_constant(matrix, constant_value) - this function multiply matrix by constant

        Params:
        matrix - matrix, that inputted by user to be multiplied
        constant_value - constant value, that inputted by user to be multipy matrix

        Returns:
        result - multiplied matrix
    """
    result = [[element * constant_value for element in rows] for rows in matrix]
    return result


def multiply_matrices(matrix_a, matrix_b):
    """
        function multiply_matrices(matrix_a, matrix_b): this function multiply two matrices

        Params:
        matrix_a - the first matrix that inputted by user
        matrix_b - the second matrix that inputted by user

        Returns:
        result - the result of multiplying two matrices
    """
    if len(matrix_a[0]) != len(matrix_b):
        print("ERROR: Number of columns in the first matrix must match the number of rows in the second matrix.")
        return None
    result = [[sum(matrix_a[i][k] * matrix_b[k][j] for k in range(len(matrix_b)))
               for j in range(len(matrix_b[0]))] for i in range(len(matrix_a))]
    return result


def transpose_matrix(matrix, transpose_type):
    """
        function transponse_matrix(matrix, transpose_type): transposes the matrix and returns the transposed matrix

        Params:
        matrix - matrix to be transposed,
        transponse_type - type of transpose

        Returns:
        result - transposed matrix
    """
    if transpose_type == 1:  # Main diagonal
        result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    elif transpose_type == 2:  # Side diagonal
        result = [[matrix[len(matrix) - j - 1][len(matrix[0]) - i - 1]
                   for j in range(len(matrix))] for i in range(len(matrix[0]))]
    elif transpose_type == 3:  # Vertical line
        result = [[matrix[i][len(matrix[0]) - j - 1] for j in range(len(matrix[0]))] for i in range(len(matrix))]
    elif transpose_type == 4:  # Horizontal line
        result = [[matrix[len(matrix) - i - 1][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]
    else:
        print("ERROR: Invalid transpose type.")
        return None
    return result


def calculate_determinant(matrix):
    """
        function calculate_determinant(matrix): calculates the determinant of a matrix

        Params:
        matrix - the size of a matrix that inputted by user

        Returns:
        det - the determinant of a matrix
    """
    if len(matrix) != len(matrix[0]):
        print("ERROR: Determinant can only be calculated for square matrices.")
        return None
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for col in range(len(matrix)):
        sub_matrix = [rows[:col] + rows[col + 1:] for rows in matrix[1:]]
        det += ((-1) ** col) * matrix[0][col] * calculate_determinant(sub_matrix)
    return det


def inverse_matrix(matrix):
    """
        function inverse_matrix(matrix): this function takes a matrix and returns the inverse matrix

        Params:
        matrix - the size of a matrix that inputted by user

        Returns:
        inv - inverse matrix
    """
    determ = calculate_determinant(matrix)
    if determ == 0:
        print("This matrix doesn't have an inverse.")
        return None

    n = len(matrix)
    identity_matrix = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    # Perform Gaussian elimination to find the inverse
    augmented_matrix = [rows + identity_matrix[i] for i, rows in enumerate(matrix)]
    for i in range(n):
        # Divide the current row by the diagonal element to make it 1
        factor = augmented_matrix[i][i]
        augmented_matrix[i] = [element / factor for element in augmented_matrix[i]]
        # Eliminate the elements below and above the diagonal
        for j in range(i + 1, n):
            factor = augmented_matrix[j][i]
            augmented_matrix[j] = [element - factor * augmented_matrix[i][index]
                                   for index, element in enumerate(augmented_matrix[j])]

    # Perform back substitution to obtain the inverse
    for i in range(n - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            factor = augmented_matrix[j][i]
            augmented_matrix[j] = [element - factor * augmented_matrix[i][index]
                                   for index, element in enumerate(augmented_matrix[j])]

    inv = [rows[n:] for rows in augmented_matrix]
    return inv


while True:
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Calculate a determinant")
    print("6. Inverse matrix")
    print("0. Exit")

    choice = input("Your choice: ")

    if choice == "1":
        matrix_a_input = read_matrix("Enter size of first matrix (rows columns): ")
        matrix_b_input = read_matrix("Enter size of second matrix (rows columns): ")
        if matrix_a_input is not None and matrix_b_input is not None:
            result_matrix = add_matrices(matrix_a_input, matrix_b_input)
            if result_matrix is not None:
                print("The result is:")
                for row in result_matrix:
                    print(*row)
    elif choice == "2":
        matrix_input = read_matrix("Enter size of matrix (rows columns): ")
        if matrix_input is not None:
            constant = float(input("Enter constant: "))
            result_matrix = multiply_matrix_by_constant(matrix_input, constant)
            print("The result is:")
            for row in result_matrix:
                print(*row)
    elif choice == "3":
        matrix_a_input = read_matrix("Enter size of first matrix (rows columns): ")
        matrix_b_input = read_matrix("Enter size of second matrix (rows columns): ")
        if matrix_a_input is not None and matrix_b_input is not None:
            result_matrix = multiply_matrices(matrix_a_input, matrix_b_input)
            if result_matrix is not None:
                print("The result is:")
                for row in result_matrix:
                    print(*row)
    elif choice == "4":
        matrix_input = read_matrix("Enter size of matrix (rows columns): ")
        if matrix_input is not None:
            print("1. Main diagonal")
            print("2. Side diagonal")
            print("3. Vertical line")
            print("4. Horizontal line")
            transpose_choice = int(input("Your choice: "))
            transposed_matrix = transpose_matrix(matrix_input, transpose_choice)
            if transposed_matrix is not None:
                print("The result is:")
                for row in transposed_matrix:
                    print(*row)
    elif choice == "5":
        matrix_input = read_matrix("Enter size of matrix (rows columns): ")
        if matrix_input is not None:
            determinant = calculate_determinant(matrix_input)
            print(determinant)
    elif choice == "6":
        matrix_input = read_matrix("Enter size of matrix (rows columns): ")
        if matrix_input is not None:
            inverse = inverse_matrix(matrix_input)
            if inverse is not None:
                print("The result is:")
                for row in inverse:
                    # Відображення з двома знаками після коми
                    formatted_row = ["{:.2f}".format(element) for element in row]
                    print(*formatted_row)
    elif choice == "0":
        break
