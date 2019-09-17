def date ():
	d=int(input("input day:"))
	m=int(input("input month:"))
	y=int(input("input year:"))
	if d in range(1,32) and m in range(1,13) and y in range(0,2020):
		return 'True'
	else:
		return 'False'


print(date())