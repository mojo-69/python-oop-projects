class Library:
    def __init__(self):
    
        self.Book=[]
    def addBook(self):
        self.add_book=input("Enter Book Name")
        self.Book.append(f"{self.add_book}")
    def showBook(self):
        count=1
        for i in self.Book:
            print(f"{count}:{i}")
            count+=1
    def searchBook(self):
        found=False
        search_book=input("enter search Book name")
        for i in self.Book:
            if i==search_book:
                found=True
                break
        if found==True:
            print("book is found")
        else:
            print("not found")
                
            
    def deleteBook(self):
        found=False
        delete_book=input("Enter delete Book name")
        for i in self.Book:
            if i==delete_book:
                found=True
                self.Book.remove(i)
                break
        if found==True:
            print("Book deleted")
            
        else:
            print("book not available")
    def totalBook(self):
        
        if len(self.Book)==0:
            print("no book available")
        else:
            print(len(self.Book))
    
b1=Library()


while True:
    
    print("1. Add Book")
    print("2. Show Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Total Books")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        b1.addBook()

    elif choice == "2":
        b1.showBook()

    elif choice == "3":
        b1.searchBook()

    elif choice == "4":
        b1.deleteBook()

    elif choice == "5":
        b1.totalBook()

    elif choice == "6":
        print("Thank You! Visit Again")
        break

    else:
        print("Invalid Choice!")

