#total character in text


def user_input():
    line=[]
    print("enter the input (press enter twice to finish): ")
    while True:
        words=input(" ",)
        if words=="":
            break
        line.append(words)
    text=" ".join(line)#join function joins the elements of data  structure with regular intervals
    return text
   
    
def file_input():
    name=input("Enter the name of file to  be analysed : ",)
    try :
        with open("name","r") as file:
            text=file.read()
    except :
        print("file not found ")
    return text



def  count_char():

    print("Total number of charecter in the file is : ",len(user_input()))

count_char()



    






        
        
    
