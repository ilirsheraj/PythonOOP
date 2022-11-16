class MercedesBenz:
	doors = 4
	wheels = 4
	model = "G"

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


m1 = MercedesBenz("lavender")

# Python is dynamically typed, so it is simple
m1.doors += 1
print(m1.doors)

# controlling attribute access
m1.doors = "Andy"
m1.doors = 1.2
print(m1.doors)
