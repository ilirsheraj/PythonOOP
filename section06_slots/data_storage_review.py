class Employee(object):

	def __init__(self, name, surname, age, status, salary):
		self.name = name
		self.surname = surname
		self.age = age
		self.status = status
		self.salary = salary


e1 = Employee("Ilir", "Sheraj", 33, "FT", 50000)
print(e1)
print(e1.name)
print(e1.surname)

print(e1.__dict__)  # Instance namespace

e1.__dict__["pension"] = "DB"
print(e1.pension)
print(e1.__dict__)
