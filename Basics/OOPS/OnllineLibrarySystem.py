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

            self.listOfBooks.append([Title,Auther,ISBN,False])
            print(f"<><><>The Book {Title} has been added successfully <><><>")

    def show(self):
        for i in self.listOfBooks:# for every list in nested list , i will be the sublist at every iteration
            print(f"Book : {i[0]} & Auther : {i[1]}")#then for that single iteration , it will  print the first element of that sublist
    
    def removeBooks(self):
        book=input("enter the name of the book that you want to remove from the library --",)
        found=False
        for i in self.listOfBooks:
            if book==i[0]:
                self.listOfBooks.remove(i)
                found=True
        if  found:
            print("The book has been removed")
        else:
            print("The book , that you want to remove does not exsist in the library")

class member(Library):
    def __init__(self,name):
        super().__init__(name)
        self.member_info={"Yuvraj Singh":{"id":"12345"},"Rohit":{"id":"67890"},"singh":{"id":"111213"}}
        self.Borrowlist=[]
        
    def Borrow(self):
        member_name=input("Please enter the member's name :",)
        memberFound=False
        bookfound=False
        for key in self.member_info:
            if key == member_name :
                memberFound=True
                Bookname=input("Enter the name of the book to be borrowed : ",)
                
                for i in self.listOfBooks:
                    
                    if i[0] == Bookname:
                        self.Borrowlist.append(Bookname)
                        self.member_info[member_name]["Book Collection"]=self.Borrowlist
                        print(f"The book {self.Borrowlist} has been Borrowed")
                        bookfound=True
                        break
                break #stop scanning member info once we have handled this member
        
        if not memberFound:
            print(f"Error <!> : Member {member_name} not fund")

        elif not bookfound:
            print("Error <!> : Book not found")
        
        

                      
    def ShowMembers(self):  
         for name, info in self.member_info.items():
                            print(f"Name: {name}")
                            for field, value in info.items():
                                print(f"  {field}: {value}")
                                print()  # blank line between members  
    
    def Return(self):
         print()
         membername=input("Enter the Name of the member , Who is Returing the Book ",)
         Memberfound=False
         bookfound=False
         for keys in self.member_info:
              if membername == keys:
                   membername=True
                   bookName=input("Enter the name of the Book to be Returned -->",)
                   for key ,value in self.member_info.items():
                        for value ,feild in value.items():
                             if bookName in self.Borrowlist:
                                  self.Borrowlist.remove(bookName)
         if not Memberfound:
              print("Error : there is no such member ")
         elif not bookfound:
              print("Error:the Book has not been borrowed")
    
    def addMember(self):
        membername=input("Enter the name person --> ",)
        memberID=input("Enter the ID of the Perosn-->",)
        if membername in self.member_info:
             print(f"Member {membername} alreadyb exsist .")

        self.member_info[membername]={"id":memberID}

    def RemoveMember(self):
         membername=input("Enter the name person --> ",)
         if membername not in self.member_info:
              print(f"The person {membername} is not the member of library")
         self.member_info.pop(membername,None)
         print(f"The Person {membername} has been removed from the membership successfully ")
         

       
def main():
     lib=member("<><><><><><>----City Central Library----<><><><><><>")

     while True:
               
               print("\n" + "="*50)
               print()
               print("Hezlich willkommen bie Stads Zentrum Bibliothek")
               print("="*50)
               print()
               print("Biite wählen sie ein Option")
               print(">>>>>>>>>>>>MENU<<<<<<<<<<<<")
               print("1. Add Books   2. Remove Books\n3.Add Members   4. Remove Members\n5. Borrow Book   6. Return a Book ")
               print("7. Show Books Available   8. Show Member's Details")
               print()
               Choice=int(input("Enter the number of your choice of service-->",))
 
               if Choice==1:
                    lib.addBooks()
               elif Choice==2:
                    lib.removeBooks()
               elif Choice==3:
                    lib.addMember()
               elif Choice==4:
                    lib.RemoveMember()
               elif Choice==5:
                    lib.Borrow()
               elif Choice==6:
                    lib.Return()
               elif Choice==7:
                    lib.show()
               elif Choice==8:
                    lib.ShowMembers()
     
     if __name__ == "__main__":
      main()


main()







  
        
        
        
    


            



        

   
            

    

            
 
        








        




