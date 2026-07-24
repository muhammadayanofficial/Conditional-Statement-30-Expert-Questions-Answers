passport=input("Passport Available (Yes/No): ")
ticket=input("Ticket Confirmed (Yes/No): ")
weight=int(input("Enter Baggage Weight (KG): "))

if passport.lower()=="yes":
    if ticket.lower()=="yes":
        if weight<=20:
            print("Check-in Successful")
            print("Boarding Pass Issued")
        else:
            print("Extra Baggage Charges Apply")
    else:
        print("Ticket Not Confirmed")
else:
    print("Passport Required")