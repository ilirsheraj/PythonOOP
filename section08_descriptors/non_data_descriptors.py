from random import randint


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


class LuckyNumber:
	# Non-data descriptor
	def __get__(self, instance, owner):
		return randint(1, 100)

	# Lets give it precedence by implementing set (data descriptor)
	def __set__(self, instance, value):
		pass


class PersonTable:
	first_name = TextField(200)
	last_name = TextField(100)
	personal_no = LuckyNumber()

	def __init__(self, personal_no):
		self.personal_no = personal_no


p = PersonTable(personal_no=10)
print(p.personal_no)

# This will change because it has no precedence unless we make it data descriptor
print(PersonTable.personal_no)