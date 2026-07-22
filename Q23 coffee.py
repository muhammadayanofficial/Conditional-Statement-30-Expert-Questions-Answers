coffee = int(input("Coffee Cups: "))
cake = input("Cake? (Yes/No): ")

bill = coffee * 450

if cake == "Yes":
    bill += 700

if bill >= 3000:
    bill -= (bill * 10) / 100

print("Final Bill:", bill)