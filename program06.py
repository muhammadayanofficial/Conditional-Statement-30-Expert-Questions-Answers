age=int(input("Enter Age: "))
bmi=float(input("Enter BMI: "))
medical=input("Medical Certificate (Yes/No): ")

if age>=18:
    if bmi<35:
        if medical.lower()=="yes":
            print("Membership Approved")
        else:
            print("Bring Medical Certificate")
    else:
        print("Weight Too High")
else:
    print("You Must Be 18 or Older")