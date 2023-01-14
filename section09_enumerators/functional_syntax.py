from enum import Enum


class Parties(Enum):
	CPC = "Conservative party of Canada"
	LPC = "Liberal Party of Canada"
	BQ = "Block Quebeqois"
	NDP = "New Democratic Party"
	GPC = "Green Party of Canada"


# Alternative syntax
Enum("Parties", ["CPC", "LPC", "BQ", "NDP", "GPC"])
# first argument: name of enam, similar to class name
# second argument: collection of labels that become symbolic names in resulting enum

# Similar to names tuples, another alternative
Parties = Enum("Parties", "CPC LPC BQ NDP GPC")

Parties.CPC
# <Parties.CPC: 1>
# <Parties.LPC: 2>
# <Parties.GPC: 5>

# Set values for symbolic names using a list of tuples
Parties2 = Enum("Parties", [("CPC", "Conservative party of Canada"),
							("LPC", "Liberal Party of Canada"),
							("BQ", "Block Quebeqois"),
							("NDP", "New Democratic Party"),
							("GPC", "Green Party of Canada")]
				)

Parties2.CPC
#<Parties.CPC: 'Conservative party of Canada'>

# Another alternative is to use a dictionary
Parties3 = Enum("Parties", {"CPC": "Conservative party of Canada",
							"LPC": "Liberal Party of Canada",
							"BQ": "Block Quebeqois",
							"NDP": "New Democratic Party",
							"GPC": "Green Party of Canada"}
				)

Parties3.CPC
# <Parties.CPC: 'Conservative party of Canada'>
