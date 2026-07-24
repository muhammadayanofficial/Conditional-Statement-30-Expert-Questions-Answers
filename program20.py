door=input("Door Locked (Yes/No): ")
motion=input("Motion Detected (Yes/No): ")
owner=input("Owner At Home (Yes/No): ")

if door.lower()=="yes":
    if motion.lower()=="yes":
        if owner.lower()=="no":
            print("Security Alert!")
            print("Police Notified")
        else:
            print("Owner Is Home")
    else:
        print("House Is Safe")
else:
    print("Lock The Door")