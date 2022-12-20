from collections import namedtuple


EV = namedtuple("ElectricVehicle", ["range", "make", "price"])
# we can now create instances as in class
ev1 = EV(417, "Chevrolet", 42000)
# we get nice repr
print(ev1)
print(ev1.range)

EV2 = namedtuple("ElectricVehicle", ["range", "make", "price"], defaults=(100, "Tesla", 49000))
# default applied to the rightmost attributes
ev2 = EV2(200)
print(ev2)

EV3 = namedtuple("ElectricVehicle", ["range", "make", "price"], defaults=(49000, ))
ev3 = EV3(200, "Tesla")
print(ev3)

# Convert named tuple to a dictionary, use asdict
ev4 = ev3._asdict()
print(ev4)

# This is awesome: it works like an iterable, no need to define a list
EV5 = namedtuple("ElectricVehicle", "range make price", defaults=(100, "Tesla", 49000))
ev5 = EV5()
print(ev5)

# As tuples they are immutable
print(ev5.range)
# ev5,range = 54  # will not work

ev6 = EV([200, 300], "chevy", 49000)
print(ev6.range)  # reference type
print(id(ev6.range))

# We can change the list inside the tuple
ev6.range[0] = 250
print(ev6.range)
print(id(ev6.range))

# For more immutability
ev7 = EV((200, 300), "chevy", 49000)

# ev7.range[0] = 250  # impossible
