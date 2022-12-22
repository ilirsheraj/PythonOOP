# class Descriptor:
# 	pass


# Think of protocols as a contract between our object and python
# the descriptor protocol:
# __get__()
# __set__()
# __delete__()


class Descriptor:
	def __get__(self, instance, owner):
		pass

	def __set__(self, instance, value):
		pass

	def __delete__(self, instance):
		pass