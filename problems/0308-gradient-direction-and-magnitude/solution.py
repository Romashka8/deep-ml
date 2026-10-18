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
	gradient = np.array(gradient)
	m = np.sqrt(np.sum(gradient ** 2))
	return {'magnitude': m,
			'direction': gradient / m if m > 0 else np.zeros_like(gradient),
			'descent_direction': -gradient / m if m > 0 else np.zeros_like(gradient)}