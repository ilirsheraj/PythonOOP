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
		success, status = Virus.reproduce(self)
		if success:
			print(f"{self.name} just replicated in the nucleus of {self.host} cells")


class CoronaVirus(RNAVirus):
	pass
	# def infect(self):
	# 	print("A coronavirus specific method with a different signature from the parents")
	# 	raise NotImplementedError()


class SARSCov2(CoronaVirus):
	"""The parent class determines whether the virus should mutate, then the child class handles the details"""
	def mutate(self):
		print(f"The {self.name} just mutated its spike protein")


# cv = CoronaVirus("MERS", 0.1, 0.2)
# # subclass comes first, se it will not be implemented, although Virus superclass has infect() method
# # cv.infect()
# print(CoronaVirus.__mro__)
#
# # to generate 1 and 0 from getrandbits()
# for i in range(5):
# 	print(getrandbits(1))

cv = SARSCov2("original", 2.9, 1.2)
cv.infect("Tobi")

for _ in range(5):
	print(cv.reproduce(), "\n")