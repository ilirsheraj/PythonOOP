class Book:
	def __init__(self, title, author, book_type, pages):
		self.title = title
		self.author = author
		self.book_type = book_type
		self.pages = pages

	# use dunder representation
	def __repr__(self):
		return f"Book('{self.title}', '{self.author}', '{self.book_type}', {self.pages})"

	def __format__(self, format_spec):
		if format_spec == "short":
			return f"{self.title} - {self.author}"
		elif format_spec == "stealth":
			return f"A book containing exactly {self.pages}. Guess?"

		return repr(self)


b = Book("Antifragile", "Nassim Taleb", "Hardcover", 519)
# f"b"
print(f"{b}")
print(f"{b:short}")
print(f"{b:stealth}")
print("=" * 40)

print("{:short}".format(b))
print("{:stealth}".format(b))
print(format(b, "stealth"))

# print(f"{100:.3f}")
# print(format(100, ".3f"))
# print("{:.3f}".format(100))
