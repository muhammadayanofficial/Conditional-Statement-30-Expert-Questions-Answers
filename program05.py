age=int(input("Enter Car Age: "))
km=int(input("Enter KM Driven: "))
engine=input("Engine Light ON? (Yes/No): ")

if engine.lower()=="yes":
    print("Immediate Inspection Required")
else:
    if age>=5:
        if km>=50000:
            print("Full Service Needed")
        else:
            print("Basic Service Needed")
    else:
        print("Car is in Good Condition")