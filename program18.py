total=int(input("Enter Total Classes: "))
attended=int(input("Enter Attended Classes: "))

attendance=(attended/total)*100

print("Attendance =", attendance,"%")

if attendance>=75:
    print("Eligible For Exam")
elif attendance>=60:
    print("Warning: Improve Attendance")
else:
    print("Not Eligible For Exam")