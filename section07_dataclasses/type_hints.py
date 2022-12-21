from dataclasses import dataclass
from typing import Any


# defining the type in dataclass is mandatory
@dataclass(order=True)
class ElectricVehicle:
	range: int
	make: str
	price: int


# if we put int instead of str, we get a warning, but no error is given
# This is because python is dynamically-typed language, so the types are not enforced
ev = ElectricVehicle(300, 10, 25000)
print(ev)
ev2 = ElectricVehicle("Andrew", 10, 25000)
print(ev2)

# To accept any type, we import Any function from typing library
@dataclass(order=True)
class ElectricVehicle:
	range: int
	make: Any
	price: int


# Since the type of the second argument is Any, no warning will be thrown, no matter what type we provide
ev = ElectricVehicle(300, 10, 25000)
print(ev)

# If you don't want to specify any type, we use 'object', the base ancestor of everything
@dataclass(order=True)
class ElectricVehicle:
	range: object
	make: object
	price: object


ev = ElectricVehicle(300, 10, 25000)
print(ev)


# Another way is to use dots
@dataclass(order=True)
class ElectricVehicle:
	range: ...
	make: ...
	price: ...


ev = ElectricVehicle(300, 10, 25000)
print(ev)
