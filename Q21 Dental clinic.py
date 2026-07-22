patient = input("Enter Patient Name: ")
treatment = input("Treatment (Cleaning/Filling): ")
member = input("Member? (Yes/No): ")

if treatment == "Cleaning":
    bill = 3000
else:
    bill = 6000

if member == "Yes":
    bill -= (bill * 15) / 100

print("Patient:", patient)
print("Final Bill:", bill)