import math 

class shape():
    def area(self):
        return 0
    
    
class circle (shape):
    def __init__(self,r):
        self.r=r

    def area(self):
        return math.pi*self.r**2
    
class rectangle(shape):
    def __init__(self,length,breath):
        self.length=length
        self.breath=breath

    def area(self):
        return self.length*self.breath
    
class triangle (shape):
    def __init__(self,length , breath,height):
        self.length=length
        self.breath=breath
        self.height=height

    def area(self):
        return self.breath*self.height*self.length
    
shapes=[circle(3),rectangle(4,5),triangle(5,6,7)]
for i in shapes:
    print(f"the area of {i} is : {i.area()}")

        

