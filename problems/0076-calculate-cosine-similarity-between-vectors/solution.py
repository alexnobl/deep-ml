import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	if v1.size == 0 or v2.size == 0:
		raise ValueError('Input vectors cannot be empty!')
	if v1.shape != v2.shape:
		raise ValueError('Shape of vectors must be equal!')
	if np.linalg.norm(v1, ord=2) == 0 or np.linalg.norm(v2, ord=2) == 0:
		raise ValueError('Magnitude of vectors caannot be zero')
	
	return np.sum(v1 * v2) / (np.sqrt(np.sum(v1**2)) * np.sqrt(np.sum(v2**2)))
	# np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))