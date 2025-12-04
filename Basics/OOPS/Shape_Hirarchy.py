import math 

class shape():
    def area(self):

        raise NotImplementedError("this mehtod to be over wright in subclasses")
    
class circle (shape):
    def __init__(self,r):
        self.radius=r

    def area(self):
        return math.pi*self.r**2
    

        

