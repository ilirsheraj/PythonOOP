# Read-only and write-only properties
class Customers:

	loyalty_levels = {"bronze", "gold", "platinum"}

	def __init__(self, loyalty):
		self._loyalty = loyalty
		self._reviews = []

	@property
	def loyalty(self):
		return self._loyalty

	@loyalty.setter
	def loyalty(self, level):
		if level not in self.loyalty_levels:
			raise ValueError(f"Invalid loyalty {level} specified")
		self._loyalty = level


	def add_review(self, review):
		if not(type(review) == int or 0 <= review <= 10):
			raise ValueError("The review must be an integer between 0 and 10 inclusive")
		self._reviews.append(review)

	@property
	def average_review(self):
		return sum(self._reviews) / len(self._reviews)


c = Customers("gold")

c.add_review(10)
c.add_review(9)
c.add_review(7)
c.add_review(6)
# print(c.average_review())  # now because its read only, it will not work
# This will now return the value of the result as if we were calling the method
print(c.average_review)

# Convert the method into a read-only property