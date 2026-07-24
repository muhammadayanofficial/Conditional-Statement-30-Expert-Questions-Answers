internet=input("Internet Connected (Yes/No): ")
webcam=input("Webcam Working (Yes/No): ")
battery=int(input("Enter Battery Percentage: "))

if internet.lower()=="yes":
    if webcam.lower()=="yes":
        if battery>=20:
            print("Exam Started Successfully")
        else:
            print("Charge Your Laptop")
    else:
        print("Enable Webcam")
else:
    print("Connect To Internet")