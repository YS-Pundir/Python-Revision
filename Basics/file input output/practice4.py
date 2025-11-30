#for a file having numbers sepraated by commas , count the numbers of even number
with open("Numbers.txt","r") as f:
    data=f.read()
    print(data)

    num=data.split(",")
    count=0
    for value in num:
        if (int(value)%2==0):
            count+=1
    print(count)




 
   

