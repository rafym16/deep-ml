def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    import numpy as np
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
	return eigenvalues