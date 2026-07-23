print("Space Mission")

fuel = int(input("Enter Fuel Percentage: "))

if fuel >= 70:

    oxygen = input("Oxygen Available? (yes/no): ").lower()

    if oxygen == "yes":

        crew = input("Crew Ready? (yes/no): ").lower()

        if crew == "yes":
            print("Rocket Launched Successfully!")
        else:
            print("Crew Not Ready.")

    else:
        print("Oxygen Required.")

else:
    print("Not Enough Fuel.")