def decorator (times_1):
	def wrap():
		print("###")
		times_1()
		print("###")
	return wrap
	
@decorator
def times_1():
	print('Time to go home!')

times_1()	