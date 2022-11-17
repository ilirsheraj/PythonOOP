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

	def __hash__(self):
		return hash((self.title, self.author))


b = Book("Antifragile", "Nassim Taleb", "Hardcover", 519)
b1 = Book("Antifragile", "Nassim Taleb II", "Hardcover", 519)  # True
b2 = Book("Antifragile", "Nassim Taleb", "Hardcover", 519)  # False

# Instances of classes by default are hashable, however in this case ours is not because we defined dunder eq,
# which changes the rules of equality so python cannot guarantee equal hashes
# When defining __eq__ we need to make the class hashable again by defining __hash__, but this has side effects
print(hash(b))

# A better way is to take into consideration all instance attributes, we create a tuple. check code
print(hash(b) == hash(b2))
print(hash(b) == hash(b1))
