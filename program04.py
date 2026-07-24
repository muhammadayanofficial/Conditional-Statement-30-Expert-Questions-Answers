amount=int(input("Enter Order Amount: "))
distance=int(input("Enter Distance (KM): "))
prime=input("Are you Prime Member (Yes/No): ")

if amount>=200:
    if prime.lower()=="yes":
        print("Order Accepted")
        print("Free Delivery")
    else:
        if distance<=5:
            print("Delivery Charge = Rs.50")
        else:
            print("Delivery Charge = Rs.100")
else:
    print("Minimum Order should be Rs.200")