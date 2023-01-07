# from weakref import WeakKeyDictionary


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


p1 = PersonTable()
p2 = PersonTable()

# It will change all the instances, and we don't want that
p1.first_name = "Andrew"
# first name will be the same for all instances
print(p1.first_name)
print(p2.first_name)
print("=" * 40)

# Let's modify the code to avoid this: Separate the values for each instance
class TextField:

	def __init__(self, length):
		self.length = length
		self._data = {}

	def __get__(self, instance, owner):
		# return self.value
		# get() will return NOne by default if the value is not found
		return self._data.get(instance)


	def __set__(self, instance, value):
		if not type(value) == str:
			raise TypeError("Value should be a string")

		if len(value) > self.length:
			raise ValueError(f"Value cannot exceed {self.length} characters")
		# self.value = value
		self._data[instance] = value

	def __delete__(self, instance):
		pass


class PersonTable:
	first_name = TextField(200)


p1 = PersonTable()
p2 = PersonTable()
p1.first_name = "Andrew"
p2.first_name = "Bonnie"
# Now they are separate
print(p1.first_name)
print(p2.first_name)
# This introduces a memory leak, since instance is key of dictionary
print(id(p1))
print(id(p2))

# Instance as key for dictionary assume sit is hashable
# It also prevents garbage collectors form collecting it, affecting memory
# This is called "memory leak" in computer science

# weakkey dictionary: different from hard references: check library above
# Data structure that improves on the problems mentioned above: will not prevent garbage collector
# from getting rid of unused data
