def answer() :
	print(42)
answer()
def run_something(func) :
	func()
run_something(answer)
print(type(run_something))

print("")

def add_args(arg1, arg2) :
	print(arg1 + arg2)
print(type(add_args))
def run_something_with_args(func, arg1, arg2) :
	func(arg1, arg2)
run_something_with_args(add_args, 5, 9)

print("")

def sum_args(*args) :
	return sum(args)
def run_with_positional_args(func, *args) :
	return func(*args)
print( run_with_positional_args(sum_args, 1,2,3,4) )

print("")

def outer(a, b) :
	def inner(c, d) :
		return c + d
	return inner(a, b)
print(outer(4,7))

print("")

def knights(saying) :
	def inner(quote) :
		return "We are the knights who say: '%s'" % quote
	return inner(saying)

print( knights('Ni!') )

def knights2(saying) :
	def inner2() :
		return "We are the knights who say: '%s'" % saying
	return inner2

a = knights2('Duck')
b = knights2('Hasenpfeffer')

print(type(a))
print(type(b))
print(a)
print(b)

print(a())
print(b())