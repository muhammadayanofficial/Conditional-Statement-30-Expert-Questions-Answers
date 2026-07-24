days=int(input("Enter Late Days: "))
student=input("Are You Student (Yes/No): ")

if days==0:
    print("No Fine")
else:
    if student.lower()=="yes":
        if days<=5:
            print("Fine = Rs.20")
        else:
            print("Fine = Rs.100")
    else:
        if days<=5:
            print("Fine = Rs.50")
        else:
            print("Fine = Rs.200")