from typing import NamedTuple


class EVehicle(NamedTuple):
	range: int
	make: str
	price: int


ev = EVehicle(100, "Tesla", 12000)

print(ev)
print(ev.range)
print(ev.make)
print(ev.price)

# ev.range = 600  # Error: Immutable

# We can also introduce default values, always remember it comes from right to left
# so modifications should be done accordingly
class EVehicle(NamedTuple):
	range: int
	make: str
	price: int = 1200


ev2 = EVehicle(100, "Tesla")
print(ev2)
print(ev2.price)
