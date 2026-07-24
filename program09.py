age=int(input("Enter Patient Age: "))
temp=float(input("Enter Body Temperature: "))
oxygen=int(input("Enter Oxygen Level: "))

if oxygen<90:
    print("Shift Patient To ICU")
else:
    if temp>=103:
        print("Patient Needs Immediate Treatment")
    elif temp>=100:
        print("Admit Patient To Hospital")
    else:
        print("Home Medication Recommended")