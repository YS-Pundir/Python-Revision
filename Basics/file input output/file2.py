#if we do not add any mode then it will be opened in read mode
file=open('example.txt')
#reading the data
data=file.read()
#printing the data
print(data)
#always close the file 
file.close()

#way to read the line , always close the file to read the line of a file 
#if we do not close the file  and try to read  it agian , there will nothing be  printed.
file=open('example.txt','r')
line1=file.readline()
print(line1)
line2=file.readline()
print(line2)