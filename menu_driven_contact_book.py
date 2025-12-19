contacts={}
while True:
    print("\n1.Add contact")
    print("2.Search contact")
    print("3.Delete contact")
    print("4.Show all")
    print("5.exit")

    choice=input("Enter your choice from (1-5): ")
    if choice.isdigit():
        choice=int(choice)
    else:
        print("That's an invaid choice")
    

    if choice==1:
        name=input("Enter the name: ")
        number=int(input("Enter the number: "))
        contacts[name]=number      #it will print key and value
        print("Contact added")
    elif choice==2:
        name=input("Enter name to search: ")
        print(contacts,"contact not found")
    elif choice==3:
        name=input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]  #will delete both key and value
            print("Deleted")
        else:
            ("contact not found")
    elif choice==4:
        print(contacts)
    elif choice==5:
        print("exiting...")
        break
    else:
        print("You choosed an invalid choice,please enter your choice from(1-5)")

