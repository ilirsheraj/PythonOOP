class MercedezBenz:
	doors = 4
	wheels = 4
	model = "G"

	def drive(self):
		return f"A Mercedes is driving. And it is {self}\n"


# All instances will get the same attributes
m1 = MercedezBenz()
m2 = MercedezBenz()

print(f"Both instances have {m1.doors} and {m2.doors} doors, respectively")
print(f"Both instances have {m1.wheels} and {m2.wheels} wheels, respectively")
print(f"Both instances are {m1.model} and {m2.model} model, respectively")

# We need to create different attributes fir different instances
# we can add them directly
m1.color = "Black"
m2.color = "Red"
print(f"Both instances have {m1.color} and {m2.color} colors, respectively")

# Add attributes while initializing
class MercedezBenz:
	doors = 4
	wheels = 4
	model = "G"

	def __init__(self, color):  # after instance creation, but before it is returned
		self.color = color

	def drive(self):
		return f"A Mercedes is driving. And it is {self}\n"


# When creating instances, we will now have to specify the color
# print(MercedezBenz())  # Gives error because we did not specify any color
# If we defined color as default `def __init__(self, color = "black")` we can call the above statement

m1 = MercedezBenz("black")
m2 = MercedezBenz("blue")
print(m1.color)
print(m2.color)
