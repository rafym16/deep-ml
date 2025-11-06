def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.

	result = 0
	result_array = []

	if len(a) == len(b):
		for item in a:
			if len(item) == len(b):
				for i in range(len(item)):
					result += item[i]*b[i]
				result_array.append(result)
				result = 0
	else:
		result_array = -1
	return result_array