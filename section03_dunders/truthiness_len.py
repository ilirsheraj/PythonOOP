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

	# # define the bool inside the class
	# def __bool__(self):
	# 	return bool(self.pages) and not (self.pages < 1)

	# Use length dunder
	# Make sur eit works on negative numbers as well by reducing them to zero
	def __len__(self):
		return self.pages if self.pages > 0 else 0


b_neg = Book("Antifragile", "Nassim Taleb", "Hardcover", -10)
b_pos = Book("Antifragile", "Nassim Taleb", "Hardcover", 519)
b_zero = Book("Antifragile", "Nassim Taleb", "Hardcover", 0)

# Test the bool here
print(len(b_neg))
print(len(b_pos))
print(len(b_zero))
# Even after commenting out __bool__, __len__ takes over, it returns boolean again
print(bool(b_zero))
