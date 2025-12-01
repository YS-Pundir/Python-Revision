#practicing inheritence 
class UECommunity:
    def __init__(self,id, name):
        self.id=id
        self.name=name
    
    def show(self):
        print("the is of the candidate is :",self.id)
        print("the name of the candidate is : ",self.name)

class UEStudent(UECommunity):
    def __init__(self,id,name,matriculation,programe,Nationality):
        super().__init__(id,name)
        self.matriculation=matriculation
        self.programe=programe
        self.Nationality=Nationality

    def show(self):
        super().show()
        print("the matriculation number of the studet is : ",self.matriculation)
        print(f"the {self.name} is currently studing : {self.programe}")
        print(f"{self.name} is from : {self.Nationality}")

student1=UEStudent(39084376,"Yuvraj Singh Pundir",123456,"Software engineering","Indian")
student1.show()