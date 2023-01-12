from enum import Enum


class Parties(Enum):
	CPC = "Conservative party of Canada"
	LPC = "Liberal Party of Canada"
	BQ = "Block Quebeqois"
	NDP = "New Democratic Party"
	GPC = "Green Party of Canada"


# In console, the following code retrieves a list of names
Parties._member_names_
# ['CPC', 'LPC', 'BQ', 'NDP', 'GPC']

# Full association requires attribute __members__: a dictionary of all associations
Parties.__members__

# This is an instance of Parties as well
print(type(Parties.CPC))

# Shown below
print(isinstance(Parties.CPC, Parties))

# Access by name or by value
Parties("Conservative party of Canada")
# CPC
# These are equivalent
print(Parties.CPC is Parties("Conservative party of Canada"))
# True


# This is quite different from a regular class
class RegularParties(object):
	CPC = "Conservative party of Canada"
	LPC = "Liberal Party of Canada"
	BQ = "Block Quebeqois"
	NDP = "New Democratic Party"
	GPC = "Green Party of Canada"


# Now this will be string
print(type(RegularParties.CPC))
# And here it is not an instance
print(isinstance(RegularParties.CPC, RegularParties))
