password="admin123"

unlock=False

while unlock==False:
    entered_password=input("Please enter the password : ",)
    if entered_password==password:
        print("Access Granted")
        unlock=True