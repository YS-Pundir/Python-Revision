class Book:
    def __init__(self,Title,Auther,isbn,is_borrowed):
        self.Title=Title
        self.Auther=Auther
        self.isbn=isbn
        self.is_borrowed=is_borrowed

Book1=Book("Experiment of my life","Gandhi",1234,True)
print(Book1.is_borrowed)

