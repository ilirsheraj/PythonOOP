class Child:
	# define a class variable called `name`
	name = "Liam"
	def __init__(self, name):
		self.name = name


print(Child.__dict__)

# Redefine another name
c = Child("Anthony")
print(c.name)
print(c.__dict__)
print("=" * 30)

class Child:
	# define a class variable called `name`
	name = "Liam"
	def __init__(self, name=None):
		if name:
			self.name = name


c = Child("Anthony")
print(c.name)
c2 = Child()
print(c2.name)
print("=" * 30)


class Grandparent:
	name = "Robert"


class Parent(Grandparent):
	# name = "James"
	pass


class Child(Parent):
	# define a class variable called `name`
	# name = "Liam"
	def __init__(self, name=None):
		if name:
			self.name = name


c = Child()
# will inherit from next class in hierarchy
print(c.name)
