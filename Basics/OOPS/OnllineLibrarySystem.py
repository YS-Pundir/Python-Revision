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
            print(f"Book : {i[0]} & Auther : {i[1]}")#then for that single iteration , it will  print the first element of that sublist
    
    def removeBooks(self):
        book=input("enter the name of the book that you want to remove from the library --",)
       
        for i in self.listOfBooks:
            if book==i[0]:
                self.listOfBooks.remove(i)
                found=True
        if  found:
            print("The book has been removed")
        else:
            print("The book , that you want to remove does not exsist in the library")
            
        
            
lib=Library("<><><><>------ City Centre Library ------<><><><>")  


lib.removeBooks()
  
        
        
        
    


            



        

   
            

    

            
 
        








        




