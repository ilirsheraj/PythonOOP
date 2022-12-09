class Point3D:

	__slots__ = ("x", "y", "z")

	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def __repr__(self):
		class_name = self.__class__.__name__

		additional_attr = ""

		if class_name != "Point3D":
			attr = self.__class__.__dict__["__slots__"][0]
			attr_value = getattr(self, attr)
			additional_attr = f", {attr}='{attr_value}'"

		return f"{class_name}(x={self.x}, y={self.y}, z={self.z}{additional_attr})"


class ColoredPoint(Point3D):

	__slots__ = ("color",)

	def __init__(self, *args, color="black", **kwargs):
		super().__init__(*args, **kwargs)
		self.color = color


class ShapedPoint(Point3D):

	__slots__ = ("shape",)

	def __init__(self, *args, shape="sphere", **kwargs):
		super().__init__(*args, **kwargs)
		self.shape = shape


p = Point3D(1, 2, 3)
# print(p.__dict__)
print(p)

sp = ShapedPoint(1, 2, 3, shape="cube")
# print(sp.__dict__)
print(sp)
sp.shape = "circle"
print(sp.shape)
print(eval(repr(sp)))

cp = ColoredPoint(1, 2, 3, color="pink")
print(cp)
# cp.bs = "ms"
cp.color = "lavender"
print(cp.color)
