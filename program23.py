seat=input("Seat Type (Normal/VIP): ")
tickets=int(input("Enter Number Of Tickets: "))
student=input("Student (Yes/No): ")

if seat.lower()=="normal":
    bill=tickets*500
elif seat.lower()=="vip":
    bill=tickets*1000
else:
    print("Invalid Seat Type")
    exit()

if student.lower()=="yes":
    bill=bill-200

print("Total Bill =", bill)

if bill>=3000:
    print("Free Popcorn")