	def data_type(n):
	"""
	This is a function called data_type, to take one argument.
	 it compares and return results, based on the argument supplied to the function.
	 the instances handled are string length,boolean values,number less or greater than 100,returning values in a list
	"""
	if isinstance(n, basestring):
		return len(n)
 	elif isinstance(n, bool):
		return n
	elif isinstance(n, int):
		if n < 100:
			return "less than 100"
		elif n > 100:
			return "more than 100"
		else:
			return "equal to 100"
	elif isinstance(n, list):
		try:
			return n[2]
		except IndexError:
			return None
	else:
		return "no value"
