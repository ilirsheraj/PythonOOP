class Customers:

	loyalty_levels = {"bronze", "gold", "platinum"}

	def __init__(self, loyalty):
		self.set_loyalty(loyalty)

	def get_loyalty(self):
		return self.loyalty

	# Make sure the loyalty comes only from those defined within the class
	def set_loyalty(self, level):
		if level not in self.loyalty_levels:
			raise ValueError(f"Invalid loyalty {level} specified")
		self.loyalty = level


# c = Customers("Andy")
c2 = Customers("bronze")
# Now we can change loyalty to anything we want
c2.loyalty = "Andy"
print(c2.get_loyalty())


class Customers:

	loyalty_levels = {"bronze", "gold", "platinum"}

	def __init__(self, loyalty):
		self.set_loyalty(loyalty)

	def get_loyalty(self):
		return self._loyalty

	# Make sure the loyalty comes only from those defined within the class
	def set_loyalty(self, level):
		if level not in self.loyalty_levels:
			raise ValueError(f"Invalid loyalty {level} specified")
		self._loyalty = level


# Customers("Ilir")  # invalid
c = Customers("bronze")
c.loyalty = "Ilir"
# Since we made it private, it will not change
print(c.get_loyalty())

print(c.__dict__)
