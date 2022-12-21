from dataclasses import dataclass
from dataclasses import field
from functools import total_ordering


# defining the type in dataclass is mandatory
@dataclass(order=True)
class ElectricVehicle:
	range: int
	make: str = "Tesla"
	price: int = 5600


ev = ElectricVehicle(420)
print(ev)

# We can make it even fancier by using field
# with field we can do many things, not just setting the type
@dataclass(order=True)
class ElectricVehicle:
	range: int = field(compare=True)
	make: str = field(default="Tesla", compare=False)
	price: int = field(default=5600, repr=False, compare=False)


ev = ElectricVehicle(420)
print(ev)
ev2 = ElectricVehicle(421)
print(ev2)
print(ev > ev2)


# To make it even more sophisticated
@total_ordering
@dataclass
class ElectricVehicle:
	range: int = field(compare=True)
	make: str = field(default="Tesla", compare=False)
	price: int = field(default=5600, repr=False, compare=False)

	# now we explicitly define price: This is like a regular class
	def __gt__(self, other):
		if not type(self) == type(other):
			return NotImplemented

		return self.price < other.price


ev = ElectricVehicle(420)
ev2 = ElectricVehicle(421, price=56000)
print(ev > ev2)
# because of total ordering, we can also check for >= as well, not just >
print(ev >= ev2)
