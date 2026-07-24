login=int(input("Enter Login Time (24 Hours): "))
logout=int(input("Enter Logout Time (24 Hours): "))
late=int(input("Enter Late Minutes: "))

hours=logout-login

if late<=15:
    if hours>=8:
        print("Full Day")
    else:
        print("Half Day")
else:
    if late<=60:
        print("Late Attendance")
    else:
        print("Absent")