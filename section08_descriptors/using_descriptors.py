# Target in this case is to be able to define a PersonTable class that has
# a first_name attribute which is text of maximum length 200 characters
# here we use binding behavior
# the __get__ of the descriptor has the same name as the attribute: It takes absolute precedence

class TextField:
	def __init__(self, length):
		self.length = length

	def __get__(self, instance, owner):
		return self.value

	def __set__(self, instance, value):
		if not type(value) == str:
			raise TypeError("Value should be a string")

		if len(value) > self.length:
			raise ValueError(f"Value cannot exceed {self.length} characters")

		self.value = value

	def __delete__(self, instance):
		pass


class PersonTable:
	first_name = TextField(200)

	def __init__(self, first_name):
		self.__dict__["first_name"] = first_name


# p = PersonTable()
# p.first_name = "a" * 30
# print(p.first_name)

p = PersonTable("Robbie")
p.first_name = "Liam"
print(p.__dict__)

# we get what the descriptor provides (Liam)
print(p.first_name)
