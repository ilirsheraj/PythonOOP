l = ["Andy", 7]

# a = {l: "BS"}  # Will give error: list is not hashable

# Use the built-in hash() function to do th same
try:
	hash(l)
except TypeError:
	print(f"List is not hashable")

name_str = "Ilir"
num_int = 7
tpl = (name_str, num_int)
print(hash(name_str))
print(hash(num_int))
print(hash(tpl))

# Criteria for an object to be hashable:
# 1 - Can be compared to other objects
# 2 - If it compares equal, it shares the same hash with the other object
# 3 - Hash value never changes over its lifetime

print(id(name_str))

# If we redefine it, the id will change because python builds a new object
# while the old one is collected by garbage collector (GC)
name_str = "Like"
print(id(name_str))