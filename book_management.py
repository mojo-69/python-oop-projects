class BookManagement:
    def __init__(self):
        self.book_id = int(input("Book ID: "))
        self.book_name = input("Book Name: ")
        self.book_author = input("Book Author: ")
        self.book_price = int(input("Book Price: "))

    def display_details(self):
        print("\n===== Book Details =====")
        print(f"Book ID      : {self.book_id}")
        print(f"Book Name    : {self.book_name}")
        print(f"Book Author  : {self.book_author}")
        print(f"Book Price   : ₹{self.book_price}")

    def discount(self):
        if self.book_price >= 500:
            discount_price = self.book_price - (self.book_price * 10) / 100
            print(f"Discount Price : ₹{discount_price}")
        else:
            print("No Discount Available")

    def book_status(self):
        if self.book_price >= 1000:
            print(f"{self.book_name} is a Premium Book")
        else:
            print(f"{self.book_name} is a Normal Book")


# Object
book = BookManagement()

# Menu
while True:
    
    print("1. Display Details")
    print("2. Discount Price")
    print("3. Book Status")
    print("4. Exit")

    option = int(input("Enter your choice: "))

    if option == 1:
        book.display_details()

    elif option == 2:
        book.discount()

    elif option == 3:
        book.book_status()

    elif option == 4:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
