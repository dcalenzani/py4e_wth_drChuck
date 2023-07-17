# 3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.

sth = input("Enter Hours: ")
str = input("Enter Rate: ")
flh = float(sth)
flr = float(str)
if flh > 40 :
    #this is payment + overtime
    rgp = flh * flr
    otp = (flh - 40.0) * (flr * 0.5)
    xcs = rgp + otp
else:
    #this is normal payment
    xcs = flh * flr
print("Pay:", xcs)
