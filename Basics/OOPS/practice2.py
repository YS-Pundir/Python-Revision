#Example Create a class to represent a Car.
#  The car have two attributes: color and brand. 
# Include a method that displays the car's color and brand.
class Car:
    def __init__(self,colour,brand):
        self.colour=colour
        self.brand=brand
    
    def show(self):
        print("the colour of the car is :",self.colour)
        print("the brand of the car is : ",self.brand)
    
car1=Car("Blue","TATA")
car1.show()
