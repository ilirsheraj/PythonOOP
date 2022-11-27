class TempVirus:

	attr = "some_class_attribute"
	attr_other = "some_other_class_attribute"

	def __init__(self, attr):
		self.attr = attr


# 1- check the __dict__
v1 = TempVirus("instance attribute")
print(v1.attr)
print(v1.__dict__)

# 2 - If attr not in instance dictionary, python checks the class namespace
# This is not in instance dictionary, but it comes from class namespace
print(v1.attr_other)
print(type(v1).__dict__)

# 3 - If not in class namespace, python will check up the classes hierarchy until it
# reaches the object and then throws error
# instance -> class -> superclass(s) -> object, else AttributeError
# This gives error
# print(v1.imaginary)

# To figure out parent class
print(TempVirus.__bases__)

# Method resolution order (MRO)
print(TempVirus.__mro__)
