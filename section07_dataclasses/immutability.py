from dataclasses import dataclass
from dataclasses import field


@dataclass(order=True)
class ElectricVehicle:
	range: int = field(compare=True)
	make: str = field(default="Tesla", compare=False)
	price: int = field(default=5600, repr=False, compare=False)


ev = ElectricVehicle(100, "BMW", 140000)
print(ev)

# data classes are mutable
ev.range = 200
print(ev)


# We can make dataclasses immutable using read-only property
class ElectriVehicle2:

	def __init__(self, range, make, price):
		self.__range = range
		self.__make = make
		self.__price = price

	@property
	def range(self):
		return self.__range

	@property
	def make(self):
		return self.__make

	@property
	def price(self):
		return self.__price


ev = ElectriVehicle2(100, "BMW", 140000)
print(ev.__dict__)
# ev.make = "Tesla"  # We cannot change it now


# To make fields immutable in dataclass is very easy using frozen
@dataclass(order=True, frozen=True)
class ElectricVehicle:
	range: int = field(compare=True)
	make: str = field(default="Tesla", compare=False)
	price: int = field(default=5600, repr=False, compare=False)


ev = ElectricVehicle(100, "BMW", 140000)
print(ev)
# data classes are immutable
# ev.range = 200  # NOw its impossible to change
# print(ev)

# Since dataclass is immutable, it became hashable by default so we can use instances
# of this dataclass as dictionary keys

bs = {
	ElectriVehicle2(100, "BMW", 140000): {
		"customers": 10,
		"tags": ["dream car", "superb"]
	}
}
print(bs)


# We can change the hashable status of each field
@dataclass(order=True, frozen=True)
class ElectricVehicle:
	range: int = field(compare=True, hash=False)
	make: str = field(default="Tesla", compare=False)
	price: int = field(default=5600, repr=False, compare=False)


ev1 = ElectricVehicle(100, "BMW", 140000)
ev2 = ElectricVehicle(120, "BMW", 140000)

print(hash(ev1), hash(ev2))
