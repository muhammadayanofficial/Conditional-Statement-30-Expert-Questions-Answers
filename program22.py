fuel=input("Enter Fuel Type (Petrol/Diesel): ")
liter=float(input("Enter Liters: "))
member=input("Member Card (Yes/No): ")

if fuel.lower()=="petrol":
    bill=liter*272
elif fuel.lower()=="diesel":
    bill=liter*280
else:
    print("Invalid Fuel Type")
    exit()

if member.lower()=="yes":
    discount=bill*0.05
    bill=bill-discount

print("Total Bill =", bill)