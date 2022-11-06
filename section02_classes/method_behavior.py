class MercedezBenz:
	doors = 4
	wheels = 4
	model = "G"


# We encapsulate behavior in functions, for example
def drive():
	return "A car is being driven"


# Invoke the function to get the return
print(drive())

# To add behavior to the class we define functions in its body
class MercedezBenz:
	doors = 4
	wheels = 4
	model = "G"

	def drive(self):
		return self


# Create an instance and print its identity
m1 = MercedezBenz()
print(m1.drive())

# Test that m1 is the same as m1.drive
print(m1 == m1.drive())

# Use object identity to confirm the above one
print(m1 is m1.drive())

# m1 is not MercedezBenz() blueprint, it is simply the instance
print(m1 == MercedezBenz)
print("=" * 30)

# Update the method
class MercedezBenz:
	doors = 4
	wheels = 4
	model = "G"

	def drive(self):
		return f"A Mercedes is driving. And it is {self}\n"


m3 = MercedezBenz()
m4 = MercedezBenz()

# The instances are the same, so they will not return the same objects
print(m3.drive())
print(m4.drive())

# Let's trace drive: It is a function
print(MercedezBenz.drive)
# Let's confirm it is a function indeed
print(type(MercedezBenz.drive))

# When we look at the instance, it turns out to be a method of the object if we don't invoke ot
print(m3.drive)
print(type(m3.drive))
print(m4.drive)
print(type(m4.drive))
