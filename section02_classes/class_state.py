class MercedesBenz:
	doors = 2
	wheels = 4


# These attributes live in the class' namespace and are accessible by __dict__
print(MercedesBenz.__dict__)
print("=" * 40)

# Change the attributes: We modified the blueprint in this way
MercedesBenz.doors = 4
# Create new attributes
MercedesBenz.model = "G"
# Check the namespace again
print(MercedesBenz.__dict__)
print("=" * 40)

# Create some instances
m1 = MercedesBenz()
m2 = MercedesBenz()

print(m1.doors)
print(m2.doors)
print(m1.model)
print(m2.model)
