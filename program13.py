vehicle=input("Enter Vehicle (Bike/Car): ")
hours=int(input("Enter Parking Hours: "))
vip=input("VIP Member (Yes/No): ")

if vip.lower()=="yes":
    print("Free Parking")
else:
    if vehicle.lower()=="bike":
        print("Parking Fee =", hours*20)
    elif vehicle.lower()=="car":
        print("Parking Fee =", hours*50)
    else:
        print("Invalid Vehicle Type")