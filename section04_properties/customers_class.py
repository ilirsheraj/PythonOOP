class Customers:

	def __init__(self, loyalty):
		self.loyalty = loyalty


c1 = Customers("bronze")
c2 = Customers("gold")
c3 = Customers("platinum")


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


for customer in [c1, c2, c3]:
	print(f"Your discount is {get_discount(customer):.0%}")
