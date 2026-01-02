import numpy as np
from scipy import stats

def confidence_interval(data: list[float], confidence_level: float = 0.95) -> dict:
	"""
	Calculate confidence interval for population mean.
	
	Args:
		data: Sample data
		confidence_level: Confidence level (default 0.95)
	
	Returns:
		Dictionary containing:
		- mean: Sample mean (point estimate)
		- standard_error: Standard error of the mean
		- margin_of_error: Margin of error
		- lower_bound: Lower bound of CI
		- upper_bound: Upper bound of CI
		- confidence_level: Confidence level used
	"""
	# Your code here
    from math import sqrt
    n = len(data)
    mean = np.mean(data)
    std = np.std(data, ddof=1)
    standard_error = std/sqrt(n)
    df = n - 1
    alpha = 1 - confidence_level 
    t_critical = stats.t.ppf(1 - (alpha/2), df)
    margin_of_error = t_critical * standard_error
    upper_bound = mean + margin_of_error
    lower_bound = mean - margin_of_error

    result = {
        'mean': mean,
  