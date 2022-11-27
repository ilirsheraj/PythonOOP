# Read-only and write-only properties
class Customers:

	loyalty_levels = {"bronze", "gold", "platinum"}

	def __init__(self, loyalty):
		self._loyalty = loyalty

	loyalty = property()  # it will reside in Customers.__dict__

	# If we want a read-only property, we define getter only. We wont be able to set
	# @loyalty.getter
	@property
	def loyalty(self):
		return self._loyalty
	#
	# # If we want a write-only property, we define setter only
	# @loyalty.setter
	# def loyalty(self, level):
	# 	if level not in self.loyalty_levels:
	# 		raise ValueError(f"Invalid loyalty {level} specified")
	# 	self._loyalty = level

# print(Customers.__dict__)
c = Customers("platinum")
print(c.loyalty)
c.loyalty = "gold"
# print(c._loyalty)