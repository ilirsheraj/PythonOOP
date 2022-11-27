class Virus:
	# name
	# reproduction_rate
	# resistance
	# host
	# viral_load
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

			return True, f"Virus reproduced in {self.host}. Viral load: {int(self.load)}"

		raise AttributeError("Virus needs to infect a host before being able to reproduce")


v = Virus("chandipura", 1.2, 1.1)
v.infect("animal1")
print(v.reproduce())
print(v.host)
print(v.load)

# Will define 2 new classes and inherit from Virus
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


r = RNAVirus("HIV", 1.1, 0.2)
r.infect("monkey0")
print(r.reproduce())
print(r.genome)

d = DNAVirus("Hepatitis", 2.1, 0.2)
d.infect("sheep1")
print(d.reproduce())
print(d.genome)
