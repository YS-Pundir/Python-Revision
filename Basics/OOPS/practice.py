#Write a class for representing rectangle which has two attributes length, and width.
#  Implement two functions to calculate area and perimeter respectively.
class rectangle :
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def Area(self):
        return self.length*self.width
    
    def perimeter(self):
        return 2*(self.length+self.width)
    
shape=rectangle(3,2)
print(shape.Area())
print(shape.perimeter())

    


