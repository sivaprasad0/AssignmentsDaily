name=input("enter a palindrme: ")

l= len(name)
i=0
count=0
for i in range(0,(l+1)//2):
	if name[i]==name[l-1-i]:
		pass
	else:
		count=count+1
		break

if count==0:
	print(name," is palindrome")
else:
	print(name,"is not a palindrome")
