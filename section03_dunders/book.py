class Book:
	def __init__(self, title, author, book_type, pages):
		self.title = title
		self.author = author
		self.book_type = book_type
		self.pages = pages


b = Book("Antifragile", "Nassim Taleb", "Hardcover", 519)
print(b.__dict__)
print(b)  # just the output of repr() built-in function
print(repr(b))

# Customize the representation using __repr__
class Book:
	def __init__(self, title, author, book_type, pages):
		self.title = title
		self.author = author
		self.book_type = book_type
		self.pages = pages

	def __repr__(self):
		return f"The title is {self.title}"


b1 = Book("Antifragile", "Nassim Taleb", "Hardcover", 519)
print(b1)

b2 = Book("America's Bank", "Roger Lowenstein", "Paperback", 360)
print(b2)

