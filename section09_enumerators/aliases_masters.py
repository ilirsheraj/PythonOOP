from enum import Enum


class Parties(Enum):
	CPC = "Conservative party of Canada"
	CPoC = "Conservative party of Canada"
	LPC = "Liberal Party of Canada"
	BQ = "Block Quebeqois"
	NDP = "New Democratic Party"
	GPC = "Green Party of Canada"


# Master name
Parties.CPC

# aliased name
Parties.CPoC

# Value
Parties("Conservative party of Canada")

# We always get the same member
print(Parties.CPC is Parties.CPoC is Parties("Conservative party of Canada"))
# True, all point out to CPC

# In console we can also see the mapping
Parties._value2member_map_
# {'Conservative party of Canada': <Parties.CPC: 'Conservative party of Canada'>,
# 'Liberal Party of Canada': <Parties.LPC: 'Liberal Party of Canada'>,
# 'Block Quebeqois': <Parties.BQ: 'Block Quebeqois'>,
# 'New Democratic Party': <Parties.NDP: 'New Democratic Party'>,
# 'Green Party of Canada': <Parties.GPC: 'Green Party of Canada'>}
