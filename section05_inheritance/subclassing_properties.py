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

	# Add a variant property that counts the available variants out there
	known_variants = ["alpha", "beta", "gamma", "epsilon"]

	def __init__(self, variant):
		super().__init__("SARSCovid2", 2.49, 1.3)
		self.variant = variant

	def mutate(self):
		print(f"The {self.name} just mutated its spike protein")

	@property
	def variant(self):
		return self._variant

	@variant.setter
	def variant(self, value):
		if value.lower() not in self.known_variants:
			raise ValueError("Expected a known variant of concern")

		self._variant = value.lower()


cv = SARSCov2("ALPHA")
print(cv.variant)
print(cv.__dict__)

# cv.variant = "SOMETHING ELSE"
cv.variant = "beta"
print(cv.variant)


# Let's inherit the property and modify it so that double mutant can set the variant
# without being limited by known variants
# class DoubleMutant(SARSCov2):
#
# 	@SARSCov2.variant.setter
# 	def variant(self, value):
# 		self._variant = value.lower()
#
#
# dv = DoubleMutant("New Variant")
# print(dv.variant)
# print(dv.__dict__)


# The longer way to do the same
class DoubleMutant(SARSCov2):

	@property
	def variant(self):
		print("Getter from the subclass")
		return self._variant

	@variant.setter
	def variant(self, value):
		self._variant = value.lower()

	@variant.deleter
	def variant(self):
		del self._variant


dv = DoubleMutant("New Variant")
print(dv.variant)
print(dv.__dict__)
