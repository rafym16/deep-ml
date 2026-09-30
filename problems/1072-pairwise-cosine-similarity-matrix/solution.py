import numpy as np

def pairwise_cosine_similarity(X):
    # Your code here
    X = np.array(X)
    dot_product = np.dot(X, X.T)

    norm = np.linalg.norm(X, axis=1, keepdims=True)

    l2_norm = norm @ norm.T

    safe_denominator = np.where(l2_norm == 0, 1.0, l2_norm)

    cosine_sim = dot_product / safe_denominator

    return cosine_sim