class Employee(object):
	# Define attributes you want slots to support
	__slots__ = ("name", "surname", "age", "status", "salary", "__dict__")

	def __init__(self, name, surname, age, status, salary):
		self.name = name
		self.surname = surname
		self.age = age
		self.status = status
		self.salary = salary


e = Employee("Ilir", "Sheraj", 33, "FT", 50000)
print(e.__dict__)

e.nickname = "Like"
print(e.__dict__)
