def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    import numpy as np
    result = []
    matrix_array = np.asarray(matrix)
    for item in matrix_array:
        multiplication = item * scalar
        result.append(multiplication)
	return result