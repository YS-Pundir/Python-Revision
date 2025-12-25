#total character in text
with open("sample.txt",'r') as file:
    text=file.read()
    print(len(text))