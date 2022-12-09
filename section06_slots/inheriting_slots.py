class Employee(object):
	# Define attributes you want slots to support
	__slots__ = ("name", "surname", "age", "status", "salary")

	def __init__(self, name, surname, age, status, salary):
		self.name = name
		self.surname = surname
		self.age = age
		self.status = status
		self.salary = salary


class Developer(Employee):
	pass


d = Developer("Ilir", "Sheraj", 33, "FT", 80000)
print(d.name)
print(d.__dict__)

d.favorite_language = "python"
print(d.__dict__)

class BusinessAnalyst(Employee):

	__slots__ = "experience"


bs = BusinessAnalyst("Vlad", "Roberts", 29, "FT", 67000)
print(bs.name, bs.surname)
# Since we defined slot, it has no dictionary
# print(bs.__dict__)
# Also we cannot add new attribute
# bs.favorite_book = "Thinking fat and slow"
print(bs)
