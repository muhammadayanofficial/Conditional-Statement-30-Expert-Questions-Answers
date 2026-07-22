chairs = int(input("Number Of Chairs: "))
tables = int(input("Number Of Tables: "))

bill = (chairs * 2500) + (tables * 6000)

if bill >= 50000:
    discount = (bill * 15) / 100
    bill -= discount

elif bill >= 25000:
    discount = (bill * 10) / 100
    bill -= discount

print("Final Bill:", bill)