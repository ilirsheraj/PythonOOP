# class Book:
# 	def __init__(self, title, author, book_type, pages):
# 		self.title = title
# 		self.author = author
# 		self.book_type = book_type
# 		self.pages = pages
#
#
# b = Book("Antifragile", "Nassim Taleb", "Hardcover", 519)
# print(b.__dict__)
# print(b)  # just the output of repr() built-in function
# print(repr(b))

# Customize the representation using __repr__
# class Book:
# 	def __init__(self, title, author, book_type, pages):
# 		self.title = title
# 		self.author = author
# 		self.book_type = book_type
# 		self.pages = pages
#
# 	# use dunder representation
# 	def __repr__(self):
# 		return f"The title is {self.title}"
#
# 	# use dunder string
# 	def __str__(self):
# 		return f"{self.title} by {self.author} in {self.book_type}"
#
#
# b1 = Book("Antifragile", "Nassim Taleb", "Hardcover", 519)
# print(b1)
# print(str(b1))
# print("=" * 40)
#
# b2 = Book("America's Bank", "Roger Lowenstein", "Paperback", 360)
# print(b2)
# print(str(b2))

# __str__ -> informal and readable for the end user
# __repr__ -> more developer/code user oriented: The goal is to return a string that
# represents the object more fully/ describes more fully. It should include all the details
# that a developer would need to recreate the instance.

# Let's make the repr more complete
# class Book:
# 	def __init__(self, title, author, book_type, pages):
# 		self.title = title
# 		self.author = author
# 		self.book_type = book_type
# 		self.pages = pages
#
# 	# use dunder representation
# 	def __repr__(self):
# 		return f"Attributes: {self.title}, {self.author}, {self.book_type}, {self.pages}"
#
# 	# use dunder string
# 	def __str__(self):
# 		return f"{self.title} by {self.author} in {self.book_type}"
#
#
# b1 = Book("Antifragile", "Nassim Taleb", "Hardcover", 519)
# print(b1)
# print(str(b1))
# print("=" * 40)
#
# b2 = Book("America's Bank", "Roger Lowenstein", "Paperback", 360)
# print(b2)
# print(str(b2))
# print("=" * 40)
#
# print(b1.__dict__)
#
# # Evaluate as valid python code directly into a new instance
# print(eval("2+2"))
# print(eval("None"))
# eval("print('do nothing')")
#
# print(eval(repr(b1)))  # This is invalid syntax, so lets change the code accordingly


class Book:
	def __init__(self, title, author, book_type, pages):
		self.title = title
		self.author = author
		self.book_type = book_type
		self.pages = pages

	# use dunder representation
	def __repr__(self):
		return f"Book('{self.title}', '{self.author}', '{self.book_type}', {self.pages})"

	# # use dunder string
	# def __str__(self):
	# 	return f"{self.title} by {self.author} in {self.book_type}"


b1 = Book("Antifragile", "Nassim Taleb", "Hardcover", 519)
print(repr(b1))
print(eval(repr(b1)))

b2 = Book("Americas Bank", "Roger Lowenstein", "Paperback", 360)
print(repr(b2))
print(eval(repr(b2)))

