class Customers:

	loyalty_levels = {"bronze", "gold", "platinum"}

	def __init__(self, loyalty):
		self.set_loyalty(loyalty)

	def get_loyalty(self):
		return self.__loyalty

	# Make sure the loyalty comes only from those defined within the class
	def set_loyalty(self, level):
		if level not in self.loyalty_levels:
			raise ValueError(f"Invalid loyalty {level} specified")
		self.__loyalty = level


c = Customers("bronze")
c.__loyalty = "Ilir"

print(c.get_loyalty())

print(c.__dict__)
# {'_Customers__loyalty': 'bronze', '__loyalty': 'Ilir'}
# Notice `_Customers' getting inside

print(c._Customers__loyalty)
