no = int(input("enter number for which table is needed: "))

range_start=int(input("enter range start"))
range_end=int(input("enter range end"))

for i in range(range_start,range_end+1):
	print(no," * ",i," = ",no*i)
