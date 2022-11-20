def get_discount(customer):
	discounts = {
		"bronze": 0.1,
		"gold": 0.2,
		"platinum": 0.35
	}
	discount = discounts.get(customer.loyalty, None)

	if not discount:
		raise ValueError("Could not determine the customer's discount")
	return discount


class Customers:

	loyalty_levels = {"bronze", "gold", "platinum"}

	def __init__(self, loyalty, membership=0):
		# self.set_loyalty(loyalty)
		self.loyalty = loyalty
		self.membership = membership

	def get_membership(self):
		return self._membership

	def set_membership(self, value):
		if value < 0 or value > 34:
			raise ValueError("Invalid membership years")
		self._membership = value

	def get_loyalty(self):
		return self._loyalty

	# Make sure the loyalty comes only from those defined within the class
	def set_loyalty(self, level):
		if level not in self.loyalty_levels:
			raise ValueError(f"Invalid loyalty {level} specified")
		self._loyalty = level

	# Use properties
	loyalty = property(fget=get_loyalty, fset=set_loyalty)
	membership = property(fget=get_membership, fset=set_membership)


c1 = Customers("bronze")
print(c1.loyalty)

print(c1.__dict__)

# We can change loyalty
c1.__dict__["loyalty"] = "platinum"
# It is still bronze
print(c1.loyalty)

c1.__dict__["loyalty"] = "gold"
c1.loyalty  # platinum

print(c1.__dict__)

# property is in the class, not instance
print(Customers.__dict__)
