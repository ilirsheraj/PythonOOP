from collections import namedtuple
from dataclasses import make_dataclass
from dataclasses import dataclass


# behind the scenes, namedtuples are just tuples
EVNT = namedtuple("ElectricVehicle", ["range", "make", "price"])
LEVNT = namedtuple("LuxuryElectricVehicle", ["mini_display", "scent_system", "internet"])

EVDC = make_dataclass("ElectricVehicle", ["range", "make", "price"])

ev1 = EVNT(100, "BMW", 74000)
print(ev1)
ev2 = LEVNT(100, "BMW", 74000)
print(ev2)
# This turns out to be true, because the elements of the tuple are the same
print(ev1 == ev2)


@dataclass
class LuxuryElectricVehicle:
	mini_display: int
	scent_system: str
	internet: bool


@dataclass
class ElectricVehicle:
	range: int
	make: str
	price: bool


# They will not be the same, unless customized to be so
ev3 = LuxuryElectricVehicle(100, "BMW", 74000)
print(ev3)
ev4 = ElectricVehicle(100, "BMW", 74000)
print(ev4)
print(ev3 == ev4)

# The other issue is that named tuples are always immutable
# dataclasses are mutable, but can be converted into immutable by using frozen argument

# Defaults to named tuples are applied to rightmost attributes first.
# with dataclasses, the order is much more clear

# Dataclasses are real dataclasses with a lot of functionality that comes with classes
# named tuples are tuples, have many uses, but have some limitations as mentioned before
# Dataclsses are new additions to python with advantages in memory and access speed
