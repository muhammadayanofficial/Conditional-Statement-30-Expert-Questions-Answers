Salary=float(input("Enter your salary:"))
Experience=int(input("Enter your Experience:"))
Performance=int(input("Performance:")) 

#1= Very poor 
#2= Poor
#3= Average 
#4= Good 
#5= Excellent

if Experience >=5 and Performance >=4:
    bonus = Salary * 0.20

elif Experience <=5 and Performance >=4:
    bonus = Salary * 0.10

elif Performance == 3:
    bonus = Salary * 0.05

else:
    bonus = 0

print("Bonus:", bonus)

salary = Salary + bonus


print("Final Salary ", salary)