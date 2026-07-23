print("Museum Security")

ticket = input("Ticket Available? (yes/no): ").lower()

if ticket == "yes":

    bag = input("Bag Checked? (yes/no): ").lower()

    if bag == "yes":

        camera = input("Carrying Camera? (yes/no): ").lower()

        if camera == "yes":
            print("Photography Pass Required.")
        else:
            print("Welcome to the Museum.")

    else:
        print("Bag Checking Required.")

else:
    print("Please Buy a Ticket.")