from functools import total_ordering


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


# Total ordering, realizing that __eq__ and __gt__ is already implemented,
# it will take care of all other comparisons. We could have used any dunder here
Book = total_ordering(Book)

b = Book("Antifragile", "Nassim Taleb", "Hardcover", 519)
b1 = Book("How Asia Works", "Joe Studwell", "Paperback", 472)
# Now all comparisons are supported by default
print(b == b1)
print(b < b1)
print(b <= b1)
print(b > b1)
print(b >= b1)
