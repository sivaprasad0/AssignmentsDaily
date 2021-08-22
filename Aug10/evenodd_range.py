start=int(input("start no"))
end=int(input("end no"))

command=input("even or odd")

if(command=="even"):
	for i in range(start,end+1):
		if(i%2==0):
			print(i," is even")
else:
        for i in range(start,end+1):
                if(i%2!=0):
                        print(i," is odd")

