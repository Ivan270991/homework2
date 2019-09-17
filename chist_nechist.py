#chistaya

def function(a,b):
	s=a**2+b**2
	return s+2*a*b

print(function(2,1))



#nechistaya

a=[1,2,3,4,5]
def dubble(i):
	return i*2

a=list(map(dubble,a))
print(a)# это ведь нечистая функция)))



#chistaya

dubble_1 =list(map (lambda x : x*2, [1,2,3,4,5] ))

print (dubble_1)