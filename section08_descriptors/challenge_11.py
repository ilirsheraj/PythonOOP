class SATScore:

	def __init__(self, score=400):
		self.score = score

	def __set_name__(self, owner, name):
		self.name = name

	def __get__(self, instance, owner):
		if instance is None:
			return self

		return instance.__dict__.get(f"SATScore_{self.name}")

	def __set__(self, instance, value):
		if not type(value) == int:
			raise TypeError("Score must be an integer")

		if not 400 <= value <= 1600:
			raise ValueError("The score must fall between 400 and 1600")

		instance.__dict__[f"SATScore_{self.name}"] = value


# Define a descriptor for GRE
class GREScore:

	def __init__(self, score=130):
		self.score = score

	def __set_name__(self, owner, name):
		self.name = name

	def __get__(self, instance, owner):
		if instance is None:
			return self

		return instance.__dict__.get(f"GREScore_{self.name}")

	def __set__(self, instance, value):
		if not type(value) == int:
			raise TypeError("Score must be an integer")

		if not 130 <= value <= 340:
			raise ValueError("The score must fall between 130 and 340")

		instance.__dict__[f"GREScore_{self.name}"] = value


class StudentProfile:
	sat = SATScore()  # class variable pointing to a descriptor
	gre = GREScore()

	def __init__(self, name=None, sat=400, gre=130):
		self.name = name
		self.sat = sat
		self.gre = gre

	def __repr__(self):
		return f"StudentProfile(name='{self.name}', sat={self.sat}, gre={self.gre})"


# Create a default instance
sp = StudentProfile()
print(sp)
print(sp.__dict__)

sp2 = StudentProfile("Liza", 1200, 130)
print(sp2.__dict__)

# sp2.sat = 2000  # error, as expected
# sp2.gre = 1234  # error again
