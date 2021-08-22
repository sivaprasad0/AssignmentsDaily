Fruits = []

while True:

	print("1.Add Fruit")
	print("2.Delete Fruit")
	print("3.Search fruit by name and rate")
	print("4.Change fruit name and rate")
	print("5.Display")
	print("6.Exit")

	
	ch = input("Enter choice: ")
	if ch.isdigit():
		print("choice taken.")
	else:
		print("you entered wrong choice")
		continue
	ch= int(ch)

	if ch == 1 :
		#Adding Fruit
		name = input("Enter fruit name")
		rate = int(input("Enter price"))
		Fruits.append([name,rate])
		i=1
		for item in Fruits:
			print(1i'.',item)
			i+=1
	elif ch == 2:
		#Delete Fruit
		print(Fruits)
		name = input("Enter fruit name")
		rate = int(input("Enter price"))
		Fruits.remove([name,rate])
		i=1
		for item in Fruits:
			print(i'.',item)
			i+=1
	elif ch == 3:
		#Search Fruit

		while True:
			print("1.Search with name")
			print("2.Search with rate")
			ch = int(input("Enter your Choice"))

			if ch == 1:
				fname = input("Enter fruit name")
				for i in Fruits:
					if i[0] == fname:
						print("Fruit exists in list")
					else:
						print("Fruit doesn't exists!")
			if ch == 2:
				n = int(input("Enter rate"))
				for frate in Fruits:
					if i[1] == frate:
						print("Fruit exists")
					else:
						print("Fruit doesn't exists")

	elif ch == 4:
		#Change fruit by name and rate
		print("1.Change by name")
		print("2.Change by rate")
		choice = int(input("Enter your choice"))
		if choice == 1:
			fname = input("Enter fruit name")
			for i in Fruits:
				if i[0] == fname:
					nname = input("Enter new name")
					i[0] = nname
					print("updated list", i)
				else:
					print("Invalid name")
		if choice == 2:
			frate = int(input("Enter rate"))
			for i in Fruits:
				if i[1] == frate:
					nrate = int(input("Enter new price"))
					i[1] == nrate
					print("updated list", i)

				else:
					print("Invalid rate")
	elif ch == 5:

		#Display
		i=1
		for item in Fruits:
			print(i'.',item)
			i+=1

	elif ch == 6:
		break;
	else:
		print("Invalid Choice")

