def v():
	a=int(input("input year:"))
	if a%4!=0 or (a%100==0 and a%400!=0):
		print('no')
	else:
		print('yes')

print(v())		
	