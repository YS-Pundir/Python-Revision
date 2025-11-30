#adding the file name and the mode of the file is set to r , which means read
#w means to write
file=open('example.txt','r')
#to read a file
data=file.read()
#printing the data the was readed 
print(data)