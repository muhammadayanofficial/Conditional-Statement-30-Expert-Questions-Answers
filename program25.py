cars=int(input("Enter Number Of Cars: "))
ambulance=input("Ambulance Present (Yes/No): ")
signal=input("Current Signal (Red/Green): ")

if ambulance.lower()=="yes":
    print("Turn Signal Green Immediately")
else:
    if cars>=20:
        print("Keep Green Signal Longer")
    elif signal.lower()=="red":
        print("Wait For Green Signal")
    else:
        print("Traffic Moving Normally")