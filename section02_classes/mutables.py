class Tire:
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


m1 = MercedesBenz()
m2 = MercedesBenz()
print(m1.tires)
print(m2.tires)
print("=" * 40)
# if we modify for m1, we will affect m2 as well
m1.tires.append(Tire(kind="spare", distance_covered=100))
print(m1.tires)
print(m2.tires)

m3 = MercedesBenz()
print(m3.tires)
