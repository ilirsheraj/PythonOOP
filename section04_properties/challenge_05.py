class DNABase:

	def __init__(self, nucleotide):
		# Attribute name will be base, not nucleotide
		self.base = nucleotide

	@staticmethod
	def _validate_and_standardize(base):
		# allow for standard bases: adenine, thymine, cytosine, guanine
		allowed = [("a", "adenine"), ("c", "cytosine"), ("g", "guanine"), ("t", "thymine")]

		for b in allowed:
			if base.lower().strip() in b:
				# return the full name for the base
				return b[1]
		# If not matched
		return False

	def set_base(self, base):
		valid_base = self._validate_and_standardize(base)

		if valid_base:
			self._base = valid_base

		else:
			raise ValueError(f"{base} is not a recognized DNA nucleotide")

	def get_base(self):
		return self._base

	base = property(fget=get_base, fset=set_base)

	def __repr__(self):
		return f"{type(self).__name__}(nucleotide='{self.base}')"


b1 = DNABase("T")
print(b1)

# b1.base = "chaos"  # will not work

# b2 = DNABase("Them")  # will not work

b2 = DNABase("A")
print(b2)