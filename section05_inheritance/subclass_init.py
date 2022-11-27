from random import getrandbits


class Virus:

	def __init__(self, name, reproduction_rate, resistance):
		self.name = name
		self.reproduction_rate = reproduction_rate
		self.load = 1
		self.host = None

	def infect(self, host):
		self.host = host

	def reproduce(self):
		if self.host is not None:
			self.load += (1 + self.reproduction_rate)

			should_mutate = getrandbits(1)
			print(f"Should mutate {should_mutate}")
			if should_mutate:
				try:
					self.mutate()
				except AttributeError:
					pass
			return True, f"Virus reproduced in {self.host}. Viral load: {int(self.load)}"

		raise AttributeError("Virus needs to infect a host before being able to reproduce")


class RNAVirus(Virus):
	genome = "ribonucleic"

	def reproduce(self):
		success, status = Virus.reproduce(self)
		if success:
			print(f"{self.name} just replicated in the cytoplasm of {self.host} cells")


class DNAVirus(Virus):
	genome = "deoxyribonucleic"

	def reproduce(self):
		success, status = super().reproduce()
		# success, status = Virus.reproduce(self)
		if success:
			print(f"{self.name} just replicated in the nucleus of {self.host} cells")


class CoronaVirus(RNAVirus):
	pass
	# def infect(self):
	# 	print("A coronavirus specific method with a different signature from the parents")
	# 	raise NotImplementedError()


class SARSCov2(CoronaVirus):
	"""The parent class determines whether the virus should mutate, then the child class handles the details"""

	def __init__(self, variant):
		super().__init__("SARSCovid2", 2.49, 1.3)
		self.variant = variant

	def mutate(self):
		print(f"The {self.name} just mutated its spike protein")


cv = SARSCov2("Omicron")
print(cv)
print(cv.reproduction_rate)
print(cv.__dict__)

# parent-child class relationship defined using inheritance
# where the child defined as init only for the purpose of calling the parent init


# In python this is uneccessary
class Parent:
	def __init__(self):
		print("Parent init")


# whether we call __init__, we inherit it by default
# if we comment it out it will again work, unless we want something special
# Python will go up until it reaches object
class Child(Parent):
	# def __init__(self):
	# 	super().__init__()
	pass


c = Child()
