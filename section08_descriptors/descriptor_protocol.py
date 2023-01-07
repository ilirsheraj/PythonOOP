# class Descriptor:
# 	pass


# Think of protocols as a contract between our object and python
# the descriptor protocol:
# __get__()    -> retrieve something
# __set__()    -> set something
# __delete__() -> delete something


class Descriptor:
	# The names are official, can be changed but not recommended
	def __get__(self, instance, owner):
		pass

	def __set__(self, instance, value):
		pass

	def __delete__(self, instance):
		pass