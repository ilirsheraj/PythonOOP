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
c2 = Customers("gold")
c3 = Customers("platinum")

# This will not work because of changes from loyalty to _loyalty but once we use property it works just fine
for customer in [c1, c2, c3]:
	print(f"Your discount is {get_discount(customer):.0%}")

d1 = Customers("bronze", 12)
print(d1.membership)

# We can also add here using +=
d1.membership += 1
print(d1.membership)

print(c1.__dict__)
