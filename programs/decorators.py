def display_params(func):

	def display_params_call(*args, **kwargs):
		for a in list(args):
			print("args", a)

		for k in kwargs.keys():
			print("kwargs", k, kwargs[k])

		return func(*args, **kwargs)
	return display_params_call


@display_params
def sum_no(a, b=0):
	result = {}
	result["r"] = a+b
	return result

@display_params
def minus(a, b=0):
	result = {}
	result["r"] = a-b
	return result

print("sum ------------", sum_no(67, b=77))
print("substraction ------------", minus(60, b=7))


# decorator with arguments

def decor_fn(operation):
	def inner_fn(func):
		def actual_fn(*args, **kwargs):
			print("arguments")
			print([a for a in args])

			print("kwargs")
			print({k:v for k, v in kwargs.items()})

			return func(*args, **kwargs)
		return actual_fn

@decor_fn("prime_no")
def prime_no(n):
