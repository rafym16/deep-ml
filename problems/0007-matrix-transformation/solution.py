import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
    try:
        A = np.array(A, dtype=float)
        T = np.array(T, dtype=float)
        S = np.array(S, dtype=float)

        det_T = np.linalg.det(T)
        det_S = np.linalg.det(S)
        
        if not (det_T == 0 or det_S == 0):
            inv_T = np.linalg.inv(T)
            transformed_matrix = inv_T @ A @ S
            return transformed_matrix
        else:
            return -1
    except Exception:
        return -1