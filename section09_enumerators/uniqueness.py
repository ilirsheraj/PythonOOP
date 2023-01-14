from enum import Enum
from enum import unique


@unique
class Parties(Enum):
	CPC = "Conservative party of Canada"  # master
	CPoC = "Conservative party of Canada"  # aliases
	LPC = "Liberal Party of Canada"
	BQ = "Block Quebeqois"
	NDP = "New Democratic Party"
	GPC = "Green Party of Canada"


# Now we get a value error
# this looks into __members__ and goes through all of them comparing member name and value
# aliases break the uniqueness
for symblic_name, member_name in Parties.__members__.items():
	print(symblic_name, member_name.name)

# We can define our own decorator
def should_be_unique(my_enum):
	is_unique = True

	for symblic_name, member_name in my_enum.__members__.items():
		if symblic_name != member_name.name:
			is_unique = False

	if not is_unique:
		raise ValueError("Enum contains aliases")

	return my_enum

@should_be_unique
class Parties(Enum):
	CPC = "Conservative party of Canada"  # master
	CPoC = "Conservative party of Canada"  # aliases
	LPC = "Liberal Party of Canada"
	BQ = "Block Quebeqois"
	NDP = "New Democratic Party"
	GPC = "Green Party of Canada"
