print("Time Machin")

machine = input("Turn On Time Machine? (yes/no): ").lower()

if machine == "yes":

    energy = int(input("Enter Energy Level: "))

    if energy >= 80:

        year = int(input("Enter Destination Year: "))

        if year >= 1900:
            print("Time Travel Successful!")
        else:
            print("Invalid Destination Year.")

    else:
        print("Not Enough Energy.")

else:
    print("Time Machine is Off.")