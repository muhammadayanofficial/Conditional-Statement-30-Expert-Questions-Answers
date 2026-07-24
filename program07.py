data=float(input("Enter Remaining Data (GB): "))
days=int(input("Enter Days Left: "))
renew=input("Auto Renewal (Yes/No): ")

if data<=1:
    if renew.lower()=="yes":
        print("Auto Renewal Enabled")
        print("Pack Will Renew Automatically")
    else:
        print("Please Renew Your Data Pack")
else:
    if days<=2:
        print("Your Pack Will Expire Soon")
    else:
        print("No Need To Renew")