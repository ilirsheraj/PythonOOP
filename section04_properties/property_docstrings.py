class Customers:

	loyalty_levels = {"bronze", "gold", "platinum"}

	def __init__(self, loyalty):
		self._loyalty = loyalty

	@property
	def loyalty(self):
		"""
		A property that returns the loyalty level of the customer
			Setting and deleting is also supported
		"""
		return self._loyalty

	@loyalty.setter
	def loyalty(self, level):
		# This is the setter
		if level not in self.loyalty_levels:
			raise ValueError(f"Invalid loyalty {level} specified")
		self._loyalty = level

	@loyalty.deleter
	def loyalty(self):
		"""Deleter multiline doctring"""
		del self._loyalty

	# loyalty = property(fget=loyalty_getter, fset=loyalty_setter, fdel=loyalty_deleter,
	# 				   doc="A property that returns the loyalty level of the customer Setting and deleting is also supported")


help(Customers.loyalty)

# We can do the same
print(Customers.loyalty.__doc__)

# There is also another way
help(Customers)
