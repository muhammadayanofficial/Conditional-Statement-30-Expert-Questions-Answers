speed = int(input("Enter Internet Speed (Mbps): "))

if speed >= 100:
    print("Excellent")

elif speed >= 50:
    print("Good")

else:
    print("Slow Internet")