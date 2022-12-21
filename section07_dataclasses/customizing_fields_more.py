from dataclasses import dataclass
from dataclasses import field


@dataclass(order=True)
class ElectricVehicle:
	range: int = field(compare=True)
	make: str = field(default="Tesla", compare=False)
	price: int = field(default=5600, repr=False, compare=False)
	luxury: bool = False


# The definition of luxury:
# a price that is greater than 80k and
# make that is BMW, Mercedes or Tesla
# We have to determine the attribute aurselves all the time, long and boring and error-prone
ev = ElectricVehicle(180, "Tesla", 40000, False)
ev = ElectricVehicle(180, "BMW", 140000, True)
ev = ElectricVehicle(180, "Audi", 30000, False)

# To make the determination of luxury according to the rules above, we can modify the code as
@dataclass(order=True)
class ElectricVehicle:
	range: int = field(compare=True)
	make: str = field(default="Tesla", compare=False)
	price: int = field(default=5600, repr=False, compare=False)
	luxury: bool = False

	def __post_init__(self):
		luxury_brands = ["BMW", "Tesla", "Mercedes"]

		self.luxury = self.make in luxury_brands and self.price > 80000


# Now luxury attribute will be determined automatically
ev = ElectricVehicle(180, "Tesla", 40000)
print(ev)
ev1 = ElectricVehicle(180, "BMW", 140000)
print(ev1)
ev2 = ElectricVehicle(180, "Audi", 30000)
print(ev2)

# We want the attribute to be overriden by the user. The above one overrides the user
@dataclass(order=True)
class ElectricVehicle:
	LUXURY_BRANDS = ("BMW", "Tesla", "Mercedes")  # Tuples are more memory efficient
	range: int = field(compare=True)
	make: str = field(default="Tesla", compare=False)
	price: int = field(default=5600, repr=False, compare=False)
	luxury: bool = None

	def __post_init__(self):
		if self.luxury is None:
			self.luxury = self.make in self.LUXURY_BRANDS and self.price > 80000


# Now luxury attribute will be determined automatically
ev = ElectricVehicle(180, "Tesla", 40000)
print(ev)
ev1 = ElectricVehicle(180, "BMW", 140000)
print(ev1)
ev2 = ElectricVehicle(180, "Audi", 30000)
print(ev2)
ev3 = ElectricVehicle(180, "Audi", 30000, True)
print(ev3)
