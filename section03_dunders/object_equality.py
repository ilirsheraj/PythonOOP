from collections import namedtuple


# class Book:
# 	def __init__(self, title, author, book_type, pages):
# 		self.title = title
# 		self.author = author
# 		self.book_type = book_type
# 		self.pages = pages
#
# 	def __repr__(self):
# 		return f"Book('{self.title}', '{self.author}', '{self.book_type}', {self.pages})"
#
#
# b = Book("Antifragile", "Nassim Taleb", "Hardcover", 519)
# b2 = Book("Antifragile", "Nassim Taleb", "Hardcover", 519)
#
# # Although the contents ar ethe same, b and b2 ar enot the same objects
# print(b == b2)
#
# # IDs are not the same
# print(id(b))
# print(id(b2))


# Let's change this behavior
class Book:
	def __init__(self, title, author, book_type, pages):
		self.title = title
		self.author = author
		self.book_type = book_type
		self.pages = pages

	def __repr__(self):
		return f"Book('{self.title}', '{self.author}', '{self.book_type}', {self.pages})"

	def __eq__(self, other):
		# Check if we are comparing something not related to book instances
		if not isinstance(other, Book):
			return False
		return self.title == other.title and self.author == other.author


b = Book("Antifragile", "Nassim Taleb", "Hardcover", 519)
b1 = Book("Antifragile", "Nassim Taleb", "Hardcover", 519)  # True
b2 = Book("Antifragile", "Nassim Taleb II", "Hardcover", 519)  # False
print(b == b1)  # True
print(b == b2)  # False

# Create a new instance from namedtuples
essay = namedtuple("essay", ["title", "author"])
e = essay("Antifragile", "Nassim Taleb")
print(type(e))
print(e.title)
print(e.author)

# b and e are instances of different classes, so false
# if we comment out if not isinstance(other, Book), it will be true because contents are the same
print(b == e)
