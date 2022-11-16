class MercedezBenz:
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


m1 = MercedezBenz()
print(m1.auto_drive())
print(MercedezBenz.auto_drive())
print(m1.create_lease())
print(MercedezBenz.create_lease())
