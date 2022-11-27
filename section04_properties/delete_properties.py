class Customers:

	loyalty_levels = {"bronze", "gold", "platinum"}

	def __init__(self, loyalty):
		self._loyalty = loyalty

	@property
	def loyalty(self):
		return self._loyalty

	@loyalty.setter
	def loyalty(self, level):
		if level not in self.loyalty_levels:
			raise ValueError(f"Invalid loyalty {level} specified")
		self._loyalty = level

	@loyalty.deleter
	def loyalty(self):
		del self._loyalty

	# We can also define them as follows (check previous code for the syntax)
	# loyalty = property(fget=loyalty_getter, fset=loyalty_setter, fdel=loyalty_deleter)

c = Customers("gold")

del c.loyalty  # now it works after defining the property

print(Customers.__dict__)  # it is not deleted from the class, only the c instance property is deleted
print(c.__dict__)
c2 = Customers("platinum")
print(c2.__dict__)
# property(fget=, fset=, fdel=)
