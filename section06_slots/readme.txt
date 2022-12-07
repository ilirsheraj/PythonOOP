Slots is a special mechanism that is used to reduce memory of the objects. 
In Python, all the objects use a dynamic dictionary for adding an attribute. 
Slots is a static type method in this no dynamic dictionary are required for allocating attribute.

In more simple terms:
SLots are class-level attributes that help python optimize memory use and execution speed. 
They are pre-specified in a tuple __slots__ = ("a", "", ...) and instead of the class storing the attribues
as dictionary, it stores them as a fixed-length array which is executed with the speed of C
However, we cannot add attributes to the class anymor elike we used to do before
