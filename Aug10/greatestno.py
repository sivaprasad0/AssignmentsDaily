a,b,c,d = input("enter 4 numbers: ").split()

a=int(a)
b=int(b)
c=int(c)
d=int(d)

if (a>b):
	x=a
else:
	x=b

if (c>d):
	y=c
else:
	y=d

if (x>y):
	print(x," is greatest number")
else:
	print(y," is greatest number")
