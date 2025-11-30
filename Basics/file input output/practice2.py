#to find id word learning exist in sample.txt
word="learning"
with open ("sample.txt","r") as f :
    data =f.read()
    if (word in data):
        print("found ")
    else:
        print("Not found")