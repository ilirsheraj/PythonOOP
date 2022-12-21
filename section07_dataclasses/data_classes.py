from dataclasses import dataclass


# Let's define a regular class and compare it to a dataclass
class RegularElectricVehicle:
	def __init__(self, _range, make, price):
		self.range = _range
		self.make = make
		self.price = price


# For dataclasses we use the decorator at the beginning and many things are taken care of
@dataclass
class ElectricVehicle:
	range: int
	make: str
	price: int


evr = RegularElectricVehicle(100, "Tesla", 50000)
print(evr)

# Better repr (of course we need to define it in normal class)
ev = ElectricVehicle(100, "Tesla", 50000)
print(ev)
