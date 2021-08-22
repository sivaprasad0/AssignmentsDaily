while True:

	sno=input("enter till what number you need series")
	if(sno.isdigit()):
		print("no entered succesfully")
		sno=int(sno)
	else:
		print("un successful entry")
		continue
	s1=1
	print(s1)
	s2=1
	print(s2)
	while s1+s2<sno+1:
		s3=s1+s2
		print(s3)
		s1=s2
		s2=s3

	command=input("if you don't want to continue, enter stop")
	if command.lower()==stop:
		break
	else:
		print("continuinfg series")
