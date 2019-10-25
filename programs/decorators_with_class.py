
class BaseDecoratorClass:
	def __init__(self, func):
		self.func = func

	def __call__(self, *args, **kwargs):
		print("argument passed .......")
		for a in args:
			print(a)

		for k in kwargs.keys():
			print("key", k, "value", kwargs.get(k))

		return self.func(*args, **kwargs)


@BaseDecoratorClass
def sumofno(a, b=0):
	return a+b

print("sumofno...........", sumofno(2, b=45))



class DecoratorswithArgs:

	def __init__(self, operation):
		self.operation = operation

	def __call__(self, func, *args, **kwargs):
		def new_fn(*args, **kwargs):
			print("operation.....", self.operation)
			print("arguments ........")
			for a in args:
				print(a)

			print("kwargs ...........")
			for k in kwargs.keys():
				print(k, kwargs.get(k))

			return func(*args, **kwargs)
		return new_fn

@DecoratorswithArgs("Addition")
def sum_of_nos(a, b, c=0):
	return {"sum": a+b+c}

print("sum_of_nos.....", sum_of_nos(23, 33, c=44))

