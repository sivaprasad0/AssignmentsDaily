start=input("start no")
if (!start.isdigit()):
	print("enter no correctly")
end=input("end no")

if (!end.isdigit()):
        print("enter no correctly")


command=input("even or odd")

if(command.lower()=="even"):
	for i in range(start,end+1):
		if(i%2==0):
			print(i," is even")
elif(command.lower()=="odd"):
        for i in range(start,end+1):
                if(i%2!=0):
                        print(i," is odd")

else:
	print("enter correct command")
