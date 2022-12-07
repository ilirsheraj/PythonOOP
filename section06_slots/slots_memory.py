# pip install pympler
from pympler.asizeof import asizeof
from sys import getsizeof


class SlottedEmployee(object):
	# Define attributes you want slots to support
	__slots__ = ("name", "surname", "age", "status", "salary")

	def __init__(self, name, surname, age, status, salary):
		self.name = name
		self.surname = surname
		self.age = age
		self.status = status
		self.salary = salary


class RegularEmployee(object):

	def __init__(self, name, surname, age, status, salary):
		self.name = name
		self.surname = surname
		self.age = age
		self.status = status
		self.salary = salary


# Keep everything the same
e1 = SlottedEmployee("Ilir", "Sheraj", 33, "FT", 50000)
e2 = RegularEmployee("Ilir", "Sheraj", 33, "FT", 50000)

# Measure their sizes
print(asizeof(e1))
print(asizeof(e2))

print(f"Memory usage was reduced by {(304 - 664) / 664:.2%} when we used slots")

# getsizeof() is misleading because it does not account for the reference object
print(getsizeof(e1))
print(getsizeof(e2))
