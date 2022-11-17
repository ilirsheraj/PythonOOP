from string import ascii_letters, punctuation
from random import choices
from copy import copy


class Password:
	"""A password which can be customized by strength and length
	Encapsulates a randomly generated password depending on user-specified strength and length
	where the latter is optimal and automatically set depending on the strength (low -> 8, mid ->12
	high -> 16). If a length is user-specified, these presets are overriden regardless of strength.

	:param strength: a measure of password's effectiveness against brute-force guessing
	:type strength: str, optimal

	:param length: the length of the password
	:type length: int, optimal
	"""

	INPUT_UNIVERSE = {
		"numbers": list(range(10)),
		"letters": list(ascii_letters),
		"punctuation": list(punctuation)
	}

	DEFAULT_LENGTHS = {
		"low": 8,
		"mid": 12,
		"high": 16
	}

	@classmethod
	def show_input_universe(cls):
		""" Returns the complete input universe from which characters are sampled

		:return: The univers eof characters from which random sampling is done to generate the passwords
		:rtype: a dictionary of lists
		"""
		return cls.INPUT_UNIVERSE

	def __init__(self, strength="mid", length=None):
		""" Constructor method """
		self.strength = strength
		self.length = length

		self._generate()

	def _generate(self):
		"""
		Password according to the strength and length specified at initialization
		:return: randomly generated password
		:rtype: str
		"""
		population = copy(self.INPUT_UNIVERSE["letters"])
		length = self.length or self.DEFAULT_LENGTHS.get(self.strength)

		if self.strength == "high":
			population += self.INPUT_UNIVERSE["numbers"] + self.INPUT_UNIVERSE["punctuation"]
		else:
			population += self.INPUT_UNIVERSE["numbers"]

		self.password = "".join(list(map(str, choices(population, k=length))))


if __name__ == "__main__":
	p_weak = Password(strength="low")
	print("Weak Password: " + p_weak.password)

	p_mid = Password(strength="mid", length=40)
	print("Mid Password: " + p_mid.password)

	p_high = Password(strength="high")
	print("Strong Password: " + p_high.password)

	p_default = Password()
	print("Default Password: " + p_default.password)
