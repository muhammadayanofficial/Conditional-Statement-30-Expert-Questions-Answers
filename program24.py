percentage=float(input("Enter Matric Percentage: "))
test=int(input("Enter Entry Test Marks: "))
documents=input("Documents Complete (Yes/No): ")

if documents.lower()=="yes":
    if percentage>=70:
        if test>=60:
            print("Admission Confirmed")
        else:
            print("Failed Entry Test")
    else:
        print("Percentage Too Low")
else:
    print("Complete Your Documents")