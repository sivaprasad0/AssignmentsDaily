#ERP Mini
erplist=[]
while True:
	print("Press 1 for add employee: ")
	print("Press 2 for delete employee: ")
	print("Press 3 to search employee with name: ")
	print("press 4 to Change employee data: ")
	print("press 5 to display employee names: ")
	print("press 6 to search if employee name is entered or not: ")
	print("press 7 to exit")

	choice = input("Enter choice: ")
	if choice.isdigit():
		print("choice taken.")
	else:
		print("you entered wrong choice")
		continue
	choice= int(choice)	
	if choice == 1: 
		ename= input("enter employee name: ")
		erplist.append(ename)
	elif choice == 2:
		print(erplist)
		ename= input("enter employee name to delete: ")
		if ename in erplist:
			erplist.remove(ename)
			print(erplist)
		else:
			print("name entered wrong")
	elif choice == 3:
		ename=input("enter employee name to search: ")
		if ename in erplist:
			eindex = erplist.index(ename)
			print("the employee is present in ",eindex+1,"position in the ERC list")
		else:
			print("the employee doesn't exists in the erplist to search the index")
	elif choice == 4:
		ename=input("enter the name you want to change: ")
		nname=input("enter the new name you want to get updated for: ")
		if ename in erplist:
			eindex=erplist.index(ename)
			erplist[eindex]=nname
		else:
			print("enter the name correctly")
			continue
	elif choice == 5:
		i=1
		if erplist==[]:
			print("the list is empty.")
			continue
		for ename in erplist:
			print(i,".",ename)
			i=i+1	
	elif choice == 6 :
		ename=input("enter employee name to search: ")
		if ename in erplist:
                        print("the employee name is entered in the ERC list")
		else:
			print("the employee is not present in the ERC list")
	elif choice == 7 :
		break;
	else:
		print("enter right choice")

