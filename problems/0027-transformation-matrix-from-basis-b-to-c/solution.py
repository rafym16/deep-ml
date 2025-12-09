def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
    import numpy as np
    inv_C = np.linalg.inv(C)
    P = inv_C @ B
	return P