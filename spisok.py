s = [16, -17, 2, 78.7, False, False, {"True": True}, 555, 12, 23, 42, "DD"]
def spisok(x):
	return type(x) is int or type(x) is float

s=sorted(list(filter(spisok,s)))
print(s)	



