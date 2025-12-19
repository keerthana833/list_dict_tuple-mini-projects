books={"python":(10,"Available"),"c":(5,"Available")}

while True:
    print("\n1.View Books")
    print("2.Issue Books")
    print("3.Return Books")
    print("4.Exit")

    choice=input("Enter your choice: ")
    

    if choice==1:
        for book,info in books.items():
            print(book ,"->copies:",info[0],"|status:",info[1])

    elif choice==2:
        name=input("Enter the name of the book: ") 
        if name in books and books[name][0]>0:
            copies=books[name][0]-1
            books[name]=(copies,"Available")
            print(books)
            print("Book Issued")
        else:
            print("Book not available")
    elif choice==3:
        name=input("Enter the name of the book: ")
        if name in books:
            copies=books[name][0]+1
            books[name]=(copies,"Available")
            print(books)
            print("Books Returned")
        else:
            print("Book not found")
    elif choice==4:
        break
    else:
        print("invalid!please enter your choice in between(1-4)")

