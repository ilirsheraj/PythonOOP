class Employee(object):
	# __slots__ = ("name", "surname", "age", "status", "salary")

	def __init__(self, name, surname, age, status, salary):
		self.name = name
		self.surname = surname
		self.age = age
		self.status = status
		self.salary = salary


# Now have a class that inherits from Employee and has a bunch of slots
class BusinessAnalyst(Employee):
	__slots__ = ("name", "surname", "age", "status", "salary", "experience")


bs = BusinessAnalyst("Vlad", "Roberts", 29, "FT", 67000)
print(bs.__dict__)
print(BusinessAnalyst.__dict__)
