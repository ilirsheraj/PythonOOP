# All classes in Python inherit from `object` type
print(object)

o1 = object()
o2 = object()

# They are different objects in memory
print(o1 == o2)
print(o1 is o2)
print(id(o1))
print(id(o2))
print(o1.__class__)
print(o1.__repr__())
print(o1.__hash__())

class TempVirus:
	pass


print(TempVirus())
# different instances
[print(TempVirus()) for i in range(3)]

# Object is callable so the two classes below are exactly the same, no matter whetehr we include object or not
class TempVirus:
	pass


class TempVirus(object):
	pass

print(TempVirus.__call__)
