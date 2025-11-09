def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# Your code here
	import numpy as np
	if vectors:
		cov = np.cov(vectors)
		return cov
	return []