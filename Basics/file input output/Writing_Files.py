#"w" is for overwriting a whole file from scratch
#"a" , means append is used to write the file from the end 
file =open("example.txt","w")

file.write("hi , i am just practicing the writing mode here")
file.close()
