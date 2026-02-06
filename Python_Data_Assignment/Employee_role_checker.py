employee=(1001,"Prithvi Singh","Security Analysis")
roles={"Examine the gurds","Admin","Distribute roles"}

print("Employee Id : ",employee[0])
print("Employee Name : ",employee[1])
print("Employee Department : ",employee[2])

has_Adimin_role="Admin" in roles

if has_Adimin_role:
    print("Admin Acces : Yes")
else:
    print("Admin access : No")
