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


print(MercedesBenz.__dict__)
print(type(MercedesBenz.__dict__))

m1 = MercedesBenz("lavender")
m1.__dict__["horse_power"] = 290
print(m1.__dict__)

# get attribute by name of "__dict__". Python goes looking for it in the namespace, then the class
# It finds it in the class. The attribute name (__dict__) points to a descriptor
# the descriptors get() is called which returns a dictionary
