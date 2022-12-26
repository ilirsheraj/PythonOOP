class TextField:

	def __init__(self, length):
		self.length = length

	def __set_name__(self, owner, name):
		print(owner)
		self.name = name

	def __get__(self, instance, owner):
		if instance is None:
			return self
		return instance.__dict__.get(f"TextField_{self.name}")

	def __set__(self, instance, value):
		if not type(value) == str:
			raise TypeError("Value should be a string")

		if len(value) > self.length:
			raise ValueError(f"Value cannot exceed {self.length} characters")

		instance.__dict__[f"TextField_{self.name}"] = value

	def __delete__(self, instance):
		del instance.__dict__[f"TextField_{self.name}"]


class PersonTable:
	first_name = TextField(200)
	last_name = TextField(100)

print(PersonTable.__dict__)

class NonPersonTable:
	first_name = TextField(200)
	last_name = TextField(100)

# Accessing from class instance, it is None: Attribute error
# However, putting the condition on __get__ fixes the problem
PersonTable.first_name

p1 = PersonTable()
p1.first_name = "Andy"
print(p1.first_name)

del p1.first_name
print(p1.first_name)
