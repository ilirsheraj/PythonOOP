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

	def __getitem__(self, item):
		# If item is a string
		if isinstance(item, str):
			# Include the book if and only if the string sequence is contained in the book title
			# Partial matching is ok
			return [book for book in self.books if item.lower() in book.title.lower()]
		return self.books[item]


b1 = Book("Homo Empathicus", "Alexander Gorlach", "Paperback", 160)
b2 = Book("Titan", "Ron Chernow", "Hardcover", 832)
b3 = Book("The Circle", "Dave Eggars", "Paperback", 497)
b4 = Book("Homo Deus", "Yuval Noah Harari", "Paperback", 464)

# Another way to do the same easily
shelf = BookShelf(capacity=10)

for b in [b1, b2, b3, b4]:
	shelf += b

# now because of __getitem__ we can access items in shelf just like in a normal list
print(shelf[0])

# Let's search inside the list using search terms, otherwise return empty list
print(shelf["Homo"])
print(shelf["bsa"])
print(shelf["homo"])
print(shelf["HOMO"])
print(shelf[2:4])
print("=" * 40)
# we can also iterate because of getiitem
for book in shelf:
	print(book)
