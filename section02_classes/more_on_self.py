class MercedezBenz:
	doors = 4
	wheels = 4
	model = "G"

	def __init__(self, color = "black"):
		self.color = color

	def drive(self):
		print(f"A Mercedez is driving. It is {self}/n")

	def auto_drive():
		return "Auto-driving for now..."


# Let's create an instance and see
m1 = MercedezBenz("pink")
print(m1.auto_drive())  # will give error
