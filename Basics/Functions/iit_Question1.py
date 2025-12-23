#marks is a global variable , which is  used in entire programe 
marks = [75, 60, 85, 90, 45, 67, 80, 92]

def calculate_average(marks):
    total=sum(marks)
    return total/len(marks)

def count_pass_fail(marks,pass_mark=50):
    #pass_count and fail count are local variable , which can only be used in ths function
    pass_count=0
    fail_count=0
    for i in marks:
        if i>=pass_mark:
            pass_count+=1
        else:
            fail_count+=1
    print(f"Student Passed: {pass_count}")
    print(f"Student Failed: {fail_count}")

def display_summary(marks):
    print("Total Students",len(marks))
    average=calculate_average(marks)
    print(f"Average Marks: {average}")
    count_pass_fail(marks)

#calling function to dispaly summary
display_summary(marks)
