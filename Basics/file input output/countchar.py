#total character in text
def  countfile():
    name=input("enter the name of the file : ",)
    try:
        with open("name",'r') as file:
            text=file.read()
            print("Total number if charecter in the file is : ",len(text))
    except:
        print("file not found")
def counttext():
    text=print("enter the text need to be analysed : ",)
    print("total number of charecter in text is : ",len(text))





        
        
    
