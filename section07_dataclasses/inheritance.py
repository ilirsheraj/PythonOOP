from dataclasses import dataclass
from dataclasses import field


# Inheritance in data classes works just like for data classes
@dataclass(order=True)
class ElectricVehicle:
	range: int = field(compare=True, hash=False)
	make: str = field(default="Tesla", compare=False)
	price: int = field(default=5600, repr=False, compare=False)


@dataclass
class LuxuriousElectricVehicles(ElectricVehicle):
	displays: int = 3
	scent_system: bool = True
	internet: bool = True
	price: int = 12000


# If we define the same attribute in parent and child, the later will override the former
# check price: included in repr and at the same time part of __dict__
lev = LuxuriousElectricVehicles(100)
print(lev)
print(lev.__dict__)
