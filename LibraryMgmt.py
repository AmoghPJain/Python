# bookcount=0
# books=[]
#
# class Library:
#     def __init__(self,no_of_books,*bookname):
#         global bookcount, books
#         self.no_of_books=no_of_books
#         self.books=bookname
#
#         books.extend(bookname)
#
#         bookcount += len(bookname)
#         # books.extend(bookname)
#
#         if(no_of_books != len(bookname)):
#             print("\nCount of books mentioned here are not matching")
#
#
#
# library1 = Library(3, "Book1", "Book2", "Book3")
# library2 = Library(3, "Book4", "Book5")
#
# print(f"Total books count: {bookcount}")
# print(f"List of books: {books}")


class Library:
    def __init__(self):

        self.no_of_books=0
        self.books=[]

    def addbook(self,book):
        self.books.append(book)
        self.no_of_books=len(self.books)

    def showinfo(self):
        print(f"\nThe library has {self.no_of_books} books. The books are:")

        for a in self.books:
            print(a)

l1 = Library()
l1.addbook("Harry Potter1")
l1.addbook("Harry Potter2")
l1.addbook("Harry Potter3")
l1.showinfo()

l2 = Library()
l2.addbook("Potter1")
l2.addbook("Potter2")
l2.addbook("Potter3")
l2.showinfo()