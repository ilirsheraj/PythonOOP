from enum import Enum
from dataclasses import dataclass


# define a class that inherits from Enum
class Parties(Enum):
	CPC = "Conservative party of Canada"
	LPC = "Liberal Party of Canada"
	BQ = "Block Quebeqois"
	NDP = "New Democratic Party"
	GPC = "Green Party of Canada"


# Whenever we want to get a party we refer to it by its code
# Parties.CPC in console looks like this: <Parties.CPC: 'Conservative party of Canada'>

# We have an iterable collection of constants
for party in Parties:
	print(party)

# enum is not sortable because it does by default not define comparison operations except __eq__
# It is very similar to data classes syntactically
@dataclass
class Party:
	member_count: int
	coalition: bool
	seats: int
