class Tire:
	"""
	Defines an automobile tire object

	:param kind: the kind of tire, e.g. operational, spare or winter
	:param distance_covered: THe distance in km the tire has covered so far
	"""

	def __init__(self, kind, distance_covered):
		self.kind = kind
		self.distance_covered = distance_covered


class MercedesBenz:
	doors = 4
	wheels = 4
	model = "G"
	tires = [Tire("operational", 10) for i in range(4)]

	def __init__(self, color="black"):
		self.color = color

	def drive(self):
		print(f"A Mercedes is driving. It is {self}/n")

	# Convert it into static method
	@staticmethod
	def auto_drive():
		return "Auto-driving for now..."

	@classmethod
	def create_lease(cls):
		print(f"A lease for {cls} will be created")


# help(Tire)
print(Tire.__dict__)
