#if we do not add any mode then it will be opened in read mode
file=open('example.txt')
#reading the data
data=file.read()
#printing the data
print(data)
#always close the file 
file.close()