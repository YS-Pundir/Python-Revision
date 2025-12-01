#Student marksheet '
class Student :
    def __init__(self,Physics,Chemistry,Maths,Physical_Education,English):
        self.Physics=Physics
        self.Chemistry=Chemistry
        self.Maths=Maths
        self.Physical_Education=Physical_Education
        self.English=English

    def average(self):
        average=(self.Chemistry+self.English+self.Maths+self.Physical_Education+self.Physics)/5
        return average
    
    def display(self):
        print(self.average())

student1=Student(99,99,88,99,66)
student1.display()