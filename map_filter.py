a=[1,2,3,4,5]
def dubble(i):
	return i*2

a=list(map(dubble,a))
print(a)


b=[1,2,3,4,5]
def chek(x):
	return x<3

b=list(filter(chek,b))
print(b)