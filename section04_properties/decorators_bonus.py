from random import randint


# Decorator: A function that takes another function as an argument, adds some functionality
# then returns it, and does all this without otherwise changing the function

# Functions as first class citizens
def ten_times(x):
	return x * 10


# Assign function to ten_x and then call ten_x as if it were a function
ten_x = ten_times
print(ten_x(7))

# Functions as arguments to other functions
def pass_three_to(func):
	what = 3
	return func(what)


print(pass_three_to(ten_times))  # careful not to pass the brackets

# Define function within another function
def outer():
	def inner():
		return "Inner function"

	s = inner()

	return s


print(outer())

# Return a function definition
def give_me_new_func():
	def new_func():
		return "The new function is returning"
	return new_func

f = give_me_new_func()
print(f())

# Closure: A Nested function that that has access to a variable in its outer enclosing scope
def greet(who):
	# outer scope how
	how = "Good morning"

	def create_greeting():
		print(f"{how},{who}")

	return create_greeting

a = greet("Like")  # a points to an instance of "create_greeting"
print(a())  # then we invoke a() as function

# Decorators a re a design pattern built on the shoulders of two giants:
# first-class functions + closures
def bingo():
	return randint(1, 47)


for i in range(3):
	print(bingo())

# Now let's enhance this function with a closure
def even_or_odd(func):
	def inner():
		num = func()
		# even or odd is decorator
		print(f"The selected number is {'even' if num % 2 == 0 else 'odd'}")
		return num

	return inner

bingo = even_or_odd(bingo)
print(bingo())

for i in range(5):
	print(bingo())
print("=" * 30)
# A better way is to use @syntax, and they will be exactly the same
# This is called syntactic sugar
@even_or_odd
def bingo():
	return randint(1, 47)


for i in range(5):
	print(bingo())
