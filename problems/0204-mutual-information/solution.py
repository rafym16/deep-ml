import numpy as np

def mutual_information(joint_prob: list[list[float]]) -> float:
	"""
	Compute the mutual information between two random variables.
	
	Args:
		joint_prob: 2D joint probability distribution P(X,Y)
	
	Returns:
		Mutual information I(X;Y)
	"""
	# Your code here
	P_xy = np.array(joint_prob)

	P_x = np.sum(P_xy, axis=1, keepdims=True)
	P_y = np.sum(P_xy, axis=0, keepdims=True)

	matmul_P_xy = P_x @ P_y

	mask = P_xy > 0

	mi = np.sum(P_xy[mask] * np.log(P_xy[mask] / matmul_P_xy[mask]))

	return max(0.0, mi)