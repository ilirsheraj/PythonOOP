class Customers:

	def __init__(self, loyalty):
		self.loyalty = loyalty

	# We can add getter and setter like in java, but it is not necessary
	def get_loyalty(self):
		return self.loyalty

	# set it
	def set_loyalty(self, level):
		self.loyalty = level


c = Customers("bronze")
print(c.get_loyalty())
# It is not necessary since we can simply say
print(c.loyalty)  # get the same thing

c.set_loyalty("bs")
print(c.loyalty)
