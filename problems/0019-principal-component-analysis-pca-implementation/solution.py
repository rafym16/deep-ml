import numpy as np

def pca(data: np.ndarray, k: int) -> np.ndarray:
    # 1. Standardization (WAJIB untuk DeepML)
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0, ddof=1)
    X = (data - mean) / std

    # 2. Covariance matrix
    cov = np.cov(X, rowvar=False)

    # 3. Eigen decomposition (matrix simetris)
    eigenvalues, eigenvectors = np.linalg.eigh(cov)

    # 4. Sort eigenvalues descending
    sorted_idx = np.argsort(eigenvalues)[::-1]
    eigenvectors = eigenvectors[:, sorted_idx]

    # 5. Ambil k principal components
    components = eigenvectors[:, :k]

    # 6. Flip sign (aturan DeepML)
    for i in range(k):
        for val in components[:, i]:
            if val != 0:
                if val < 0:
                    components[:, i] *= -1
                break

    return np.round(components, 4)
