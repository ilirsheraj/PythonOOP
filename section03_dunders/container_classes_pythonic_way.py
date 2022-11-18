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
		# Check if we are comparing something nost related to book instances
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


class BookShelf:
	def __init__(self, capacity):
		self.books = []
		self.capacity = capacity

	def add_book(self, book):
		if not isinstance(book, Book):
			raise TypeError("Only instances of Book can be added to the bookshelf")

		if not self.capacity > len(self.books):
			raise OverflowError("The Bookshelf is full")

		self.books.append(book)

	# To print the book list to avoid getting memory locatiin when printing books
	def __repr__(self):
		return str(self.books)

	# Add a new method for adding instances easily
	def __add__(self, other):
		# create an instance containing all books already there plus the new book
		if not isinstance(other, Book):
			raise TypeError("Operation supported only in instances of the Book")

		new_shelf = BookShelf(self.capacity)

		for book in self.books:
			new_shelf.add_book(book)

		new_shelf.add_book(other)
		return new_shelf

	# create this method to make addition work both ways: Operator Overloading
	def __radd__(self, other):
		if not isinstance(other, Book):
			raise TypeError("Operation supported only in instances of the Book")

		return self + other


shelf = BookShelf(capacity=10)

b1 = Book("Homo Empathicus", "Alexander Gorlach", "Paperback", 160)
b2 = Book("Titan", "Ron Chernow", "Hardcover", 832)
b3 = Book("The Circle", "Dave Eggars", "Paperback", 497)
b4 = Book("Homo Deus", "Yuval Noah Harari", "Paperback", 464)

shelf.add_book(b1)
shelf.add_book(b2)

# Now comes the magic
print(shelf + b3)
print(b3 + shelf)
# inplace add is defined by __iadd__ but when not available, __radd__ does the job
# shelf += b4  # in console only, it is supported because of __add__ and __radd__
print(bs)

# shelf did not change
print(shelf)
