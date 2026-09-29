import numpy as np


def poisson_deviance(y: np.ndarray, mu: np.ndarray) -> float:
    """Poisson deviance, using the convention 0 * log(0) = 0."""
    # Your code here
    y_log_ratio = np.where(y > 0, y * np.log(y/mu), 0)
    result = 2 * np.sum(y_log_ratio - (y - mu))
    return result

def dispersion_ratio(y: np.ndarray, mu: np.ndarray, n_params: int) -> float:
    """Pearson chi-square divided by (n - n_params)."""
    # Your code here
    pearson_chi_square = np.sum((y-mu)**2 / mu)
    result = pearson_chi_square / (len(y) - n_params)
    return result
