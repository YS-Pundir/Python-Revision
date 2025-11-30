#checking in which line does word learning exists
word="learning"
data=True
line_no=1
with open("sample.txt","r") as f:
    
    
    while(data):
        data=f.readline()
        if(word in data):
            print(line_no)
        line_no+=1

    
    
    
   
    
    
    
    
    