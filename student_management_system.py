students={}


while True:
    print("\n1.Add student")
    print("2.View All student")
    print("3.Search student")
    print("4.Exit")

    choice=int(input("Enter your choice:"))


    if choice==1:
        name=input("Enter the name of the student: ")
        marks=int(input("Enter Marks: "))
        students[name]=marks
        print("Student added")

    elif choice==2:
        if not students:
            print("Students not found")
        else:
            for name,marks in students.items():
                print(name,marks)
    
    elif choice==3:
        name=input("Enter the name of the student to search: ")
        print(students.get(name,"students not found"))

    elif choice==4:
        print("exiting....")
        break

    else:
        print("invalid choice!")
