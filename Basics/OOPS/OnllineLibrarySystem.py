class Book:
    def __init__(self,Title,Auther,isbn,is_borrowed):
        self.Title=Title
        self.Auther=Auther
        self.isbn=isbn
        self.is_borrowed=False

class Library():
    def __init__(self,name):
        self.name=name
        self.listOfBooks=[["Death","Sadguru",35713,False],["Samadhi","OSHO",384333,False],["Sambhog","OSHO",283361,False]]
        
       
        
    def addBooks(self):
        maxLim=int(input("Add the maximum limit of book that can be added at once : ",))

        print(f"the maximum limit of adding the book is {maxLim}")
        print("---------Add Books---------")

        for  i in range(maxLim): 
            print("enter the details of the book that  needed to be added ->")
            
            Title=input("enter the name of the book : ",)
            Auther=input("enter the name of the auther : ",)
            ISBN=input("enter the isbn of the book :",)

            book=Book(Title,Auther,ISBN,False)
            self.listOfBooks.append(book)
            print(f"<><><>The Book {book.Title} has been added successfully <><><>")
    def show(self):
        for i in self.listOfBooks:# for every list in nested list , i will be the sublist at every iteration
            print(i[0])#then for that single iteration , it will  print the first element of that sublist
            
lib=Library("dennf")
lib.show()

        

   
            

    

            
 
        








        




