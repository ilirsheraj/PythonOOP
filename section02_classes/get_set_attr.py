class MercedezBenz:
	doors = 4
	wheels = 4
	model = "G"

	def __init__(self, color = "black"):
		self.color = color

	def drive(self):
		print(f"A Mercedez is driving. It is {self}/n")


m1 = MercedezBenz()
print(m1)
m2 = MercedezBenz("red")
print(m2)
print(MercedezBenz.doors)
print(m1.color)
print(m1.wheels)

# Another way to get attributes is using getattr
print(getattr(m1, "color"))  # same as print(m1.color)

setattr(m2, "color", "less reddish")
print(m2.color)

# getattr and setattr in action
objs = [m1, m2]
# add attributes accross all
attribs = ["color", "doors"]
values = ["navyblue", 3]

for obj in objs:
	for attrib, val in zip(attribs, values):
		setattr(obj, attrib, val)

print(m1.color, m2.color)
print(m1.doors, m2.doors)

# Access attributes that do not exist
try:
	print(m2.wingspan)
except AttributeError as e:
	print(e)

# use getattr without error
print(getattr(m2, "wingspan", "No attribute found"))
