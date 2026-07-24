room=input("Enter Room Type (Standard/Deluxe): ")
days=int(input("Enter Number of Days: "))
members=int(input("Enter Number of Members: "))

if room.lower()=="standard":
    bill=days*3000
elif room.lower()=="deluxe":
    bill=days*5000
else:
    print("Invalid Room Type")
    exit()

if members>4:
    bill=bill+1000

print("Total Bill =", bill)

if bill>=20000:
    print("Free Breakfast Included")