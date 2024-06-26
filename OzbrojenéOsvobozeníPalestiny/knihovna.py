class Library:
    def __init__ (self,):
        self.books=[]

    def add_book(self,book):
        self.books.append(book)

    def remove_book(self,book):
        if book in self.books:
            self.books.remove(book)
        else:
            print("This book isn't in the library.")

    def list_book(self,):
        for book in library.books:
            print(book)
library=Library()
library.add_book("Powers of nature- National Geographic")
library.add_book("Le libraire-Gérard Bessette")
library.add_book("So Long and Thanks for All the Fish-Douglas Adams")
library.add_book("Vet in a spin-James Harriot")
library.add_book("Learn Python the hard way-Zed A.Shaw")
library.remove_book("Learn Python the hard way-Zed A.Shaw")
library.list_book()