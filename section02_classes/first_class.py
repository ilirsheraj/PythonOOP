class MercedezBenz:
	pass


# We have now an object and we can use identifiers
print(MercedezBenz)
print("The type of class is: ")
print(type(MercedezBenz))
print()
print("Properties of the class")
print(MercedezBenz.__bases__)
print(MercedezBenz.__name__)

# Create a new instance of the class
print(MercedezBenz())

m1 = MercedezBenz()
m2 = MercedezBenz()
# These are separate objects in memory
print(m1 == m2)
