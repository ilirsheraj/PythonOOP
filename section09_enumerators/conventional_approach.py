# The problem of storing static collection of fixed values along single dimension
# Take the example of canadian political parties before election
# Conservative party of Canada
# Liberal Party of Canada
# Block Quebequois
# New Democratic Party
# Green Party of Canada

# Normally we need to strore them as lists for electronic voting app
parties = ["CPC", "LPC", "BQ", "NDP", "GPC"]

# To make it immutable we use tuple
PARTIES = ("CPC", "LPC", "BQ", "NDP", "GPC")

for party in PARTIES:
	print(party)

# But if someone sorts the tuple, we will lose track of indices
PARTIES = sorted(PARTIES)
print(PARTIES)

# This will require us to update indices
# The savy way to save us from this in OOP is by defining enumeration (ENUM)
