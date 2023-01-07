class TextField:

	def __init__(self, length):
		self.length = length

	def __set_name__(self, owner, name):
		self.name = name

	def __get__(self, instance, owner):
		return instance.__dict__.get(f"TextField_{self.name}")

	def __set__(self, instance, value):
		if not type(value) == str:
			raise TypeError("Value should be a string")

		if len(value) > self.length:
			raise ValueError(f"Value cannot exceed {self.length} characters")

		instance.__dict__[f"TextField_{self.name}"] = value

	def __delete__(self, instance):
		pass


class PersonTable:
	# No need to specify the name of the descriptor, class variable takes care of it
	first_name = TextField(200)
	last_name = TextField(100)


p1 = PersonTable()
p1.first_name = "Andrew"
p1.last_name = "Bonnie"
print(p1.first_name)
print(p1.last_name)
