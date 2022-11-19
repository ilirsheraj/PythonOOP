from math import sqrt, hypot
from functools import total_ordering


@total_ordering
class Vector:

	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def __repr__(self):
		# Including parameter names
		# return f"Vector(x = {self.x}, y = {self.y}, z = {self.z})"
		# Excluding parameter names
		return f"Vector({self.x}, {self.y}, {self.z})"

	def __add__(self, other):
		if not isinstance(other, Vector):
			raise TypeError("Operation is only supported between instances of Vector")

		return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

	def __mul__(self, other):
		if not type(other) == int and not type(other) == float:
			raise TypeError("Operation is only supported a numeric scalar")

		return Vector(self.x * other, self.y * other, self.z * other)

	def __rmul__(self, other):
		# Just to make right multiplication valid and the operations will be delegated to __mul__
		return self * other

	def __abs__(self):  # -> abs()
		# return sqrt(self.x ** 2 + self.y ** 2 + self.z **2)
		return hypot(self.x, self.y, self.z)

	def __eq__(self, other):
		if not isinstance(other, Vector):
			return False

		return self.x == other.x and self.y == other.y and self.z == other.z

	def __hash__(self):
		# hash and equality generally are written one after the other
		return hash((self.x, self.y, self.z))

	def __le__(self, other):
		if not isinstance(other, Vector):
			return TypeError("Must be a vector")

		return abs(self) < abs(other)

	def __bool__(self):
		return bool(abs(self))

	def __getitem__(self, item):
		if type(item) == str and item.lower() in ["x", "y", "z"]:
			return eval(f"self.{item.lower()}")

		else:
			return NotImplemented


v1 = Vector(1, 2, 3)
v2 = Vector(2, 3, 6)
v3 = Vector(0, 0, 0)
print(bool(v1))
print(bool(v3))
print(abs(v1))
print(abs(v2))
print(abs(v3))
print(v1 + v2)
print(2 * v1)
print(v1 < v2)
print(v1 > v2)
print(v1 <= v2)
print(v1["x"])
print(v1["z"])
print(v1["BS"])
print(hash(v1))
