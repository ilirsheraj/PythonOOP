class Virus:
	"""
	This is called `Parent Class` or `Superclass` or `Base Class`
	"""
	pass


class RNAVirus(Virus):
	"""
	The RNAVirus class inherits from Virus class
	This is also called `derived class` or `child class` or `subclass` or `subtype`
	"""
	pass


class Coronavirus(RNAVirus):
	pass


class SARSCov2(Coronavirus):
	pass


# To check the relationship between classes we use `issublclass()` function
print(issubclass(SARSCov2, Coronavirus))  # True
print(issubclass(Coronavirus, RNAVirus))  # True
print(issubclass(RNAVirus, Coronavirus))  # False
print(issubclass(SARSCov2, Virus))  # True
