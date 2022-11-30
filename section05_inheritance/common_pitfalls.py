from random import choice
from collections import UserDict


class FunnyDict(dict):

	not_found = ["404", "wait, what?", "Try again, or dont?"]

	# Override the dunder responsible for lookup
	def __getitem__(self, item):
		if not item in self:
			return choice(self.not_found)

		return super().__getitem__(item)


rd = {
	"CAN": 38,
	"USA": 329,
	"IND": 1380
}

fd = FunnyDict({
	"CAN": 38,
	"USA": 329,
	"IND": 1380
})

# print(rd["CAR"])
print(fd["CAR"])

# There are other ways to access the values of a dictionary
print(rd.get("CAN"))
print(fd.get("CAN"))
print(fd.get("CAR"))  # This returns None, the code did not crash


# To fix it, define another method
class FunnyDict(dict):

	not_found = ["404", "wait, what?", "Try again, or dont?"]

	# Override the dunder responsible for lookup
	def __getitem__(self, item):
		if not item in self:
			return choice(self.not_found)

		return super().__getitem__(item)

	def get(self, value):
		return self.__getitem__(value)


fd = FunnyDict({
	"CAN": 38,
	"USA": 329,
	"IND": 1380
})

print(fd.get("CAR"))
print("=" * 30)


# Now we inherit from UserDict
class FunnyDict(UserDict):

	not_found = ["404", "wait, what?", "Try again, or dont?"]

	# Override the dunder responsible for lookup
	def __getitem__(self, item):
		if not item in self:
			return choice(self.not_found)

		return super().__getitem__(item)


fd = FunnyDict({
	"CAN": 38,
	"USA": 329,
	"IND": 1380
})
# Now we have consistency
print(fd.get("CAR"))
print(fd["CAR"])
print(fd.data)
