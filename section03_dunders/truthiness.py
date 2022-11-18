from functools import total_ordering


# Use total_ordering as a static method and everything will be like the previous way
@total_ordering
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

	# Define a dunder for greater than
	def __gt__(self, other):
		if not isinstance(other, Book):
			# Comparison of book and non-book object make sno sense
			return NotImplemented
		return self.pages > other.pages

	def __hash__(self):
		return hash((self.title, self.author))

	# define the bool inside the class
	def __bool__(self):
		return bool(self.pages) and not (self.pages < 1)


b_neg = Book("Antifragile", "Nassim Taleb", "Hardcover", -10)
b_pos = Book("Antifragile", "Nassim Taleb", "Hardcover", 519)
b_zero = Book("Antifragile", "Nassim Taleb", "Hardcover", 0)

# Will b evaluate to true or false?
# if b:
# 	print("Truthy")
# else:
# 	print("Falsey")
#
# # or
# print(bool(b))
# print(bool(0))

# Test the bool here
print(bool(b_neg))
print(bool(b_pos))
print(bool(b_zero))
