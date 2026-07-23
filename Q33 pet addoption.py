age = int(input("Enter your age: "))
house = input("Enter your house type (House/Appartment): ")
pet = input("Have you own a pet before (Yes/No): ")

if age >= 18:
    if house == "House":
        if pet == "yes":
            print("Eligible")
        else:
            print("Eligible but take care of your pet")
    else:("Not eligible")
else:
    print("You must be 18+ to own a pet")
        