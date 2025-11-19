# Program to check the grade of the student based on marks
marks=int(input("enter your marks:",))
if marks >=90:
    print("Congratulations , you got A grade .\n Keep it up!")
elif marks >=80 and marks<90:
    print("Well Done , oyu got B grade . \n hope you will improve it further !")
elif marks >=70 and marks<80:
    print("Good , You got C grade .\n Looking forward to see you doing better !")
elif marks >=60 and marks<70:
    print("Sufficiesnt to pass , you got D grade .\n need to word hard !")
else:
    print("Failed , you got last grade .\n Better luck next time ...")