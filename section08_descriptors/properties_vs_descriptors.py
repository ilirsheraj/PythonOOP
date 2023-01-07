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


# class PersonalTableWithDescriptor:
# 	first_name = TextField(200)


# Instead of the above, what about using properties?
# The two classes are just the same
# Adding last name and occupation means changing all the fields in code
class PersonTableWithProps:
	def __init__(self, first_name_length):
		self._TextField_first_name = None
		self.first_name_length = first_name_length

	@property
	def first_name(self):
		return self._TextField_first_name

	@first_name.setter
	def first_name(self, value):
		if not type(value) == str:
			raise TypeError("Value must be a string")

		if len(value) > self.first_name_length:
			raise ValueError(f"Value cannot exceed {self.first_name_length} characters")

		self._TextField_first_name = value

	@first_name.deleter
	def first_name(self):
		del self._TextField_first_name


p = PersonTableWithProps(200)
# p.first_name = 2 # error by type
# p.first_name = "a" * 230  # validation by length
p.first_name = "Andrew"
p.__dict__["first_name"] = "wont be able to get here"
print(p.__dict__)
print(p.first_name)


# Adding last name and occupation means changing all the fields in code
# There is no re-usability here
class PersonTableWithProps:
	def __init__(self, first_name_length, last_name_length, occupation_length):
		self._TextField_first_name = None
		self._TextField_last_name = None
		self._TextField_occupation = None

		self.first_name_length = first_name_length
		self.last_name_length = last_name_length
		self.occupation_length = occupation_length

	@property
	def first_name(self):
		return self._TextField_first_name

	@first_name.setter
	def first_name(self, value):
		if not type(value) == str:
			raise TypeError("Value must be a string")

		if len(value) > self.first_name_length:
			raise ValueError(f"Value cannot exceed {self.first_name_length} characters")

		self._TextField_first_name = value

	@first_name.deleter
	def first_name(self):
		del self._TextField_first_name

	@property
	def last_name(self):
		return self._TextField_last_name

	@last_name.setter
	def last_name(self, value):
		if not type(value) == str:
			raise TypeError("Value must be a string")

		if len(value) > self.last_name_length:
			raise ValueError(f"Value cannot exceed {self.last_name_length} characters")

		self._TextField_last_name = value

	@last_name.deleter
	def last_name(self):
		del self._TextField_last_name

	@property
	def occupation(self):
		return self._TextField_occupation

	@occupation.setter
	def occupation(self, value):
		if not type(value) == str:
			raise TypeError("Value must be a string")

		if len(value) > self.occupation_length:
			raise ValueError(f"Value cannot exceed {self.occupation_length} characters")

		self._TextField_occupation = value

	@occupation.deleter
	def occupation(self):
		del self._TextField_occupation


# As for descriptors, its only a matter of adding two lines of code
class PersonalTableWithDescriptor:
	first_name = TextField(200)
	last_name = TextField(200)
	occupation = TextField(100)
