length=int(input("Enter Password Length: "))
number=input("Contains Number (Yes/No): ")
special=input("Contains Special Character (Yes/No): ")

if length>=8:
    if number.lower()=="yes":
        if special.lower()=="yes":
            print("Strong Password")
        else:
            print("Medium Password")
    else:
        print("Weak Password")
else:
    print("Password Too Short")