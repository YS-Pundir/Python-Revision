#with syntex
with open("example.txt","a+") as f:
    data=f.read()
    print(data)
    f.write("\nthe data that i am writing right now is nothing but appending ")
    f.close()

with open("example.txt","r") as f:
    data=f.read()
    print(data)
# i have observed that the time i am running the program the sentence it written in as much number of time , which is surprising