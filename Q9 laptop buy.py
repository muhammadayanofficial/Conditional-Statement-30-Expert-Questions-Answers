brand = input("Enter Laptop Brand (Dell/HP/Lenovo): ")
quantity = int(input("Enter Quantity: "))
student = input("Are You A Student? (Yes/No): ")
warranty = input("Extra Warranty? (Yes/No): ")

price = 0
discount = 0


if brand == "Dell":
    price = 80000

elif brand == "HP":
    price = 70000

else:
    price = 65000

bill = price * quantity


if student == "Yes":
    discount += 10


if quantity >= 2:
    discount += 5


if discount > 15:
    discount = 15

discount_amount = (bill * discount) / 100
bill = bill - discount_amount


if warranty == "Yes":
    bill = bill + (5000 * quantity)

print("LAPTOP BILL")
print("Brand:", brand)
print("Quantity:", quantity)
print("Discount:", discount, "%")
print("Warranty:", warranty)
print("Final Bill:", bill)