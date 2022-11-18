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

	# Define a dunder for less than: It's not necessary anyway
	def __lt__(self, other):
		return NotImplemented

	# Define a dunder for less than or equal
	def __le__(self, other):
		return self.pages <= other.pages

	def __ge__(self, other):
		return NotImplemented

	def __hash__(self):
		return hash((self.title, self.author))


b = Book("Antifragile", "Nassim Taleb", "Hardcover", 519)
print(b)
b1 = Book("How Asia Works", "Joe Studwell", "Paperback", 472)
print(b1)
print(b == b1)
print(b != b1)

# Check whether the number of pages in book 1 is bigger
print(b > b1)
# Take another instance
# print(b > 4)  # Will throw error
print(b < b1)
print(b <= b1)
