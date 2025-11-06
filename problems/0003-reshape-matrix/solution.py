import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
    import numpy as np
    matrix = np.asarray(a)
    try:
        reshaped_matrix = np.reshape(matrix, new_shape)
        
    except ValueError:
        reshaped_matrix = []
    
    return reshaped_matrix