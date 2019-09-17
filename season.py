def season(m):
	if m<3 or m==12:
		return "Winter"
	if 3<=m<6 :
		return "Spring"
	if 6<=m<9 :
		return "Summer"
	if 9<=m<12 :
		return "Autumn"

n=1
while n<13:
	print(n)
	print(season(n))
	n+=1				
