class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, Price: ${self.price:.2f}"

    def apply_discount(self, discount):
        self.price -= self.price * discount

class EBook(Book):
    def __init__(self, title, author, price, format):
        super().__init__(title, author, price)
        self.format = format

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, Price: ${self.price:.2f}, Format: {self.format}"


title = input("Enter the book's title: ")
author = input("Enter the book's author: ")
price = float(input("Enter the book's price: "))
book = Book(title, author, price)

print("Book Information:")
print(book.display_info())

discount = float(input("Enter the discount percentage (e.g., 10 for 10%): ")) / 100
book.apply_discount(discount)
print("Discount applied.")


print("Updated Book Information:")
print(book.display_info())

title = input("Enter the eBook's title: ")
author = input("Enter the eBook's author: ")
price = float(input("Enter the eBook's price: "))
format = input("Enter the eBook's format: ")
ebook = EBook(title, author, price, format)

print("EBook Information:")
print(ebook.display_info())
