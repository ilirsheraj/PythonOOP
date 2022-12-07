class Employee(object):

	# Define attributes you want slots to support
	__slots__ = ("name", "surname", "age", "status", "salary")

	def __init__(self, name, surname, age, status, salary):
		self.name = name
		self.surname = surname
		self.age = age
		self.status = status
		self.salary = salary


e1 = Employee("Ilir", "Sheraj", 33, "FT", 50000)
print(e1.name, e1.status)

# print(e1.__dict__)  # dictionary does not exist anymore
# Not possible to extend anymore
# e1.pension = "DB"
# print(e1.pension)
