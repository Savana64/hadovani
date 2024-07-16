print("\t\n")
print ("\t bo je stvořen objekt, volá se nejdřív magic method new\n")

class Class1:

    def __init__(self):
        print("Hi! I am __init__ magic method.")

    def __new__(cls):
        print("Hi! I am __new__ magic method.") 
        return super(Class1, cls).__new__(cls)   
        
obj1=Class1()
print(("\n"))



print ("\t zipování tuplů, \n to sem sice nepatří, ale bude se mi to hodit a nechci to zapomenout\n")     # zipování tuplú

junak1 = "Ferda"
junak2 = "Pytlík"

for jun in zip((junak1, junak2),(0.25,0.3)):
    
    print(f"expexted výsledek:{jun[0],(jun[1])}")
print ("\n")

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

book1=Book("Python Crash Course","Eric Matthes", 624)
print(book1)

class myBook:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def showBookInfo(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")
book1=myBook("Python Crash Course","Eric Matthes", 624)
book1.showBookInfo()