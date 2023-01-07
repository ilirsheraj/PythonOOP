class TextField:

	def __init__(self, length):
		self.length = length

	def __set_name__(self, owner, name):
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


class PersonTableWithProps:
	def __init__(self, first_name_length):
		self._TextField_first_name = None
		self.first_name_length = first_name_length

	def get_first_name(self):
		return self._TextField_first_name

	def set_first_name(self, value):
		if not type(value) == str:
			raise TypeError("Value must be a string")

		if len(value) > self.first_name_length:
			raise ValueError(f"Value cannot exceed {self.first_name_length} characters")

		self._TextField_first_name = value

	def del_first_name(self):
		del self._TextField_first_name

	# first_name is a class variable now
	first_name = property(fget=get_first_name, fset=set_first_name, fdel=del_first_name)


class PersonTable:
	first_name = TextField(200)