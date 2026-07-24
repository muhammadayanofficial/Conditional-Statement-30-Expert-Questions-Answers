age=int(input("Enter Your Age: "))
salary=int(input("Enter Monthly Salary: "))
credit=int(input("Enter Credit Score: "))

if age>=21:
    if salary>=50000:
        if credit>=700:
            print("Loan Approved")
        elif credit>=600:
            print("Loan Approved With Guarantor")
        else:
            print("Poor Credit Score")
    else:
        print("Salary Is Too Low")
else:
    print("Not Eligible Due To Age")