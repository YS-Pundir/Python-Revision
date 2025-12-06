class Book:
    def __init__(self,Title,Auther,isbn,is_borrowed):
        self.Title=Title
        self.Auther=Auther
        self.isbn=isbn
        self.is_borrowed=False

class Library():
    def __init__(self,name):
        self.name=name
        self.listOfBooks=[]

    def addBooks(self):
        maxLim=int(input("Add the maximum limit of book that can be added at once : ",))
        print(f"the maximum limit of adding the book is {maxLim}")
        print("---------Add Books---------")

        for  i in range(maxLim): 
            print("enter the details of the book that  needed to be added ->")
            
            Title=input("eneter the name of the book : ",)
            Auther=input("enter the name of the auther : ",)
            ISBN=input("enter the isbn of the book :",)

            book=Book(Title,Auther,ISBN,False)
            self.listOfBooks.append(book)
            print(f"<><><>The Book {book.Title} has been added successfully <><><>")

        n=1
        print("Books in the libraries are the following -->")
        for i in self.listOfBooks:
            
            print(f" {n}. {book.Title} by {book.Auther}")
            n+=1

            
 
        


lib=Library("City Library")
lib.addBooks()





        




