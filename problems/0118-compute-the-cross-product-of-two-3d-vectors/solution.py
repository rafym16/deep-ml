import numpy as np

def cross_product(a, b):
    # Your code here
    vec1 = np.array(a)
    vec2 = np.array(b)
    if vec1.shape == vec2.shape:
        result = np.cross(vec1, vec2)
        return result
    pass