battery=int(input("Enter Battery Percentage: "))
charging=input("Charging (Yes/No): ")
temp=int(input("Enter Laptop Temperature: "))

if charging.lower()=="yes":
    if battery>=100:
        print("Unplug Charger")
    elif temp>70:
        print("Stop Charging")
    else:
        print("Charging Safely")
else:
    if battery<=20:
        print("Charge Your Laptop")
    else:
        print("Battery Level is Good")