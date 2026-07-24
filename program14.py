age=int(input("Enter Age: "))
student=input("Student (Yes/No): ")
distance=int(input("Enter Distance (KM): "))

if age<5:
    print("Free Ticket")
else:
    if student.lower()=="yes":
        if distance<=50:
            print("Ticket Price = Rs.100")
        else:
            print("Ticket Price = Rs.180")
    else:
        if distance<=50:
            print("Ticket Price = Rs.150")
        else:
            print("Ticket Price = Rs.250")