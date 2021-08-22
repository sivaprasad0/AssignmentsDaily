str=input("enter a string ")
subst=input("enter a substring ")

ls=len(str)
lss=len(subst)
count=0

for i in range(0,ls-lss):
	if(str[i]==subst[i]):
		for k in range(1,lss):
			if str[i+k]!=str[i+k]:
				count=count+1
				break
if count==0:
	print(subst," is substring of ",str)
else:
	print(subst," isn't substring of ",str)
