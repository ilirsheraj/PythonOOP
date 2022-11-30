# Adding new features to lists
l = [1, 10, 2.23, 21]

# To get the mean of the list we need to do it manually or use numpy
print(sum(l) / len(l))

# Extend some of the functionalities of lists

class AvgList(list):
	def average(self):
		return sum(self) / len(self)


l2 = AvgList([1, 10, 2.23, 21])
print(l2.average())


class AvgList(list):
	@property
	def average(self):
		return sum(self) / len(self)


l3 = AvgList([1, 10, 2.23, 21])
print(l3.average)


# Let's improve it even further by instantiating passing in an arbitrary number of numeric arguments
class AvgList(list):

	def __init__(self, *args):
		if args and type(args[0]) != list:
			super().__init__(args)

		else:
			super().__init__(args[0])

	@property
	def average(self):
		return sum(self) / len(self)


l4 = AvgList(1, 10, 2.23, 21)
print(l4.average)
l3 = AvgList([1, 10, 2.23, 21])
print(l3.average)
