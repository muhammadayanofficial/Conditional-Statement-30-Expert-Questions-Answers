level=int(input("Enter Water Level (%): "))
motor=input("Motor Status (On/Off): ")

if level>=100:
    print("Tank Full")
    if motor.lower()=="on":
        print("Turn Motor OFF")
elif level<=20:
    print("Water Level Low")
    if motor.lower()=="off":
        print("Turn Motor ON")
else:
    print("Water Level Normal")