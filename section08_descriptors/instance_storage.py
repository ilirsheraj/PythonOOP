class TextField:

	def __init__(self, length, filed_name):
		self.length = length
		self._data = {}
		self.field_name = filed_name

	def __get__(self, instance, owner):
		return instance.__dict__.get(f"TextField_{self.field_name}")

	def __set__(self, instance, value):
		if not type(value) == str:
			raise TypeError("Value should be a string")

		if len(value) > self.length:
			raise ValueError(f"Value cannot exceed {self.length} characters")

		instance.__dict__[f"TextField_{self.field_name}"] = value

	def __delete__(self, instance):
		pass


class PersonTable:
	first_name = TextField(200, "first_name")
	last_name = TextField(100, "last_name")


p1 = PersonTable()
p1.first_name = "Andrew"
p1.last_name = "Bonnie"
print(p1.first_name)
print(p1.last_name)

# If p1 is deleted, everything will go with it!
