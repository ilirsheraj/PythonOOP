from dataclasses import dataclass
from functools import total_ordering


# Let's define a regular class and compare it to a dataclass
@total_ordering
class RegularElectricVehicle:
	def __init__(self, _range, make, price):
		self.range = _range
		self.make = make
		self.price = price

	def __repr__(self):
		return f"{type(self).__name__}(range={self.range}, make='{self.make}', price={self.price})"

	# for object equality
	def __eq__(self, other):
		if not type(other) == type(self):
			return False

		return self.range == other.range and self.make == other.make and self.price == other.price

	def __gt__(self, other):
		if not type(other) == type(self):
			raise TypeError("Only operations between REV are supported")

		return (other.range, other.make, other.price) < (self.range, self.make, self.price)


# For dataclasses we use the decorator at the beginning and many things are taken care of
@dataclass(order=True)
class ElectricVehicle:
	range: int
	make: str
	price: int


# after defining repr we can print out a better representation
evr = RegularElectricVehicle(100, "Tesla", 50000)
print(evr)
evr2 = RegularElectricVehicle(100, "Tesla", 50000)
# print(evr == evr2)  # not equal because it is base do object's id
# after introducing the equality attribute, now they will be equal but the code above is quite long
print(evr == evr2)
# add attribute for equality
print(evr > evr2)


# Better repr (of course we need to define it in normal class)
ev = ElectricVehicle(100, "Tesla", 50000)
print(ev)
# same
print(repr(ev))

# Attribute by attribute comparison: no need for involved coding like in regular class
ev2 = ElectricVehicle(100, "Tesla", 50000)
print(ev == ev2)

# Comparison operators
print(ev >= ev2)  # not by default, but we can change it in decorator(order=True)
