scores = [72, 45, 89, 30, 60]
for score in scores:
    if score<50:
        print("Fail")
        continue
    elif score>=50:
        print("Pass")