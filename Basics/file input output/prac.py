import csv

data=[
    ["Yuvraj ","Singh","Pundir"],
    [34,77,89],
    [88,23,53]
]
try:
    # with open("machine-readable-business-employment-data-sep-2025-quarter.csv","r") as f:
    #     reader=csv.reader(f)#csv have diffrent method toi be readed properly , it can not be reded by normal method as txt file
    #     for row in reader:
    #         print(row)
    #     f.close()

    with open("machine-readable-business-employment-data-sep-2025-quarter.csv","w",newline="") as f:
        writer=csv.writer(f)
        writer=writer.writerows(data)
        
except FileNotFoundError:
    print("file  does not exsist")
except TypeError:
    print("No argument provided !!")
    

