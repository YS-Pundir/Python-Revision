import csv
with open("machine-readable-business-employment-data-sep-2025-quarter.csv","r") as f:
    reader=csv.reader(f)#csv have diffrent method toi be readed properly , it can not be reded by normal method as txt file
    for row in reader:
        print(row)
