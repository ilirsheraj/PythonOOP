from collections import UserDict


class BidirectionalDict(UserDict):
	"""
	The dictionary behaves like a normal dictionary, but it allows the user to look up in both directions
	The user can get the value form the key and the key from the value
	"""

	def __setitem__(self, key, value):

		if key in self:
			del self[key]

		if value in self:
			del self[value]

		super().__setitem__(key, value)
		super().__setitem__(value, key)

	# If an element in removed, its mirror sibling will be deleted also
	def __delitem__(self, key):
		super().__delitem__(self[key])
		super().__delitem__(key)

	def __len__(self):
		return super().__len__() // 2


bd = BidirectionalDict({"a": "b", "c": "d"})
print(bd)

print(len(bd))

bd["a"] = "v"
print(bd)

del bd["a"]
print(bd)

del bd["d"]
print(bd)

print(len(bd))

bd["i"] = "b"
print(bd)

bd.pop("i")
print(bd)

bd["i"] = "b"
bd.pop("b")

bd = BidirectionalDict({"a": "b", "c": "d"})
bd.update([("a", "Better")])
print(bd)
