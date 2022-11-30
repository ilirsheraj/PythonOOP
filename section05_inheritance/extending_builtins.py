from random import choice


population = {
	"CAN": 38,
	"USA": 329,
	"IND": 1380
}

print(population["CAN"])
# print(population["ALB"])  # key error
# This is similar to
# print(population.__getitem__("alb"))

# We want to build a dictionary where we do not get coe crash
class FunnyDict(dict):

	not_found = ["404", "wait, what?", "Try again, or dont?"]

	# Override the dunder responsible for lookup
	def __getitem__(self, item):
		if not item in self:
			return choice(self.not_found)

		return super().__getitem__(item)


population = FunnyDict({
	"CAN": 38,
	"USA": 329,
	"IND": 1380
})

print(population["CAN"])
print(population["CANADA"])

for i in range(6):
	print(population["CANADA"])
