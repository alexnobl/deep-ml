import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	# Your code here
	mag = 0
	for i in gradient:
		mag += i**2
	mag = mag**0.5
	dirc = [x/mag if mag != 0 else 0 for x in gradient]
	des_dirc = [-x for x in dirc]

	return {'magnitude':mag, 'direction':dirc, 'descent_direction':des_dirc}