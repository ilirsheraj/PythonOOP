class Customers:

	loyalty_levels = {"bronze", "gold", "platinum"}

	def __init__(self, loyalty):
		# self.set_loyalty(loyalty)
		self.loyalty = loyalty

	# remove get_loyalty()
	@property
	def loyalty(self):
		return self._loyalty

	# remove set_loyalty()
	@loyalty.setter
	def loyalty(self, level):
		if level not in self.loyalty_levels:
			raise ValueError(f"Invalid loyalty {level} specified")
		self._loyalty = level


c = Customers("bronze")
print(c.loyalty)
print(c.__dict__)

# The above class definition is the same as this one below
# decorator is a shortcut for the code below
# class Customers:
#
# 	loyalty_levels = {"bronze", "gold", "platinum"}
#
# 	def __init__(self, loyalty):
# 		# self.set_loyalty(loyalty)
# 		self.loyalty = loyalty
#
# 	loyalty = property()
# 	def loyalty_getter(self):
# 		return self._loyalty
#
# 	loyalty = loyalty.getter(loyalty_getter)
# 	def loyalty_setter(self, level):
# 		if level not in self.loyalty_levels:
# 			raise ValueError(f"Invalid loyalty {level} specified")
# 		self._loyalty = level
#
# 	loyalty = loyalty.setter(loyalty_setter)
#
#
# c = Customers("bronze")
# print(c.loyalty)
# print(c.__dict__)
