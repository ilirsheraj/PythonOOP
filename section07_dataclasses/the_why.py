# The question is how do we encapsulate data

# We want to capture the following three attributes
# EV -> Store several instances of EV
# range -> how long a car should go on a single charge
# make -> the manufacturer
# price -> how much the EV costs

# We can store them in a list
bolt = [417, "Chevrolet", 42000]
model_s = [528, "Tesla", 84000]
max30 = [100, "Mazda", 35000]

# To mak eit immutable, we can use tuple
bolt = (417, "Chevrolet", 42000)
model_s = (528, "Tesla", 84000)
max30 = (100, "Mazda", 35000)

# To access the attributes, we have to know the index for each of them
# We can use dictionary to get over the problem of index
bolt = {"range": 417, "name":"Chevrolet", "price":42000}
model_s = {"range": 528, "name":"Tesla", "price":84000}
max30 = {"range": 100, "name":"Mazda", "price":35000}

print(bolt["range"])
print(bolt.get("range"))


# We would like to get the data by attribute, and this can be done by class
class EV:
	def __init__(self, _range, make, price):
		self.range = _range
		self.make = make
		self.price = price


chev = EV(417, "Chevrolet", 42000)
print(chev.__dict__)
print(chev.range)
